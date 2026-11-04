import os, sqlite3, secrets, re, json
from datetime import datetime, timezone
from functools import wraps
from pathlib import Path
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash

ROOT = Path(__file__).resolve().parent
DB = Path(os.environ.get('AMABLE_DB', str(ROOT / 'amable.db')))
MODEL = os.environ.get('OLLAMA_MODEL', 'codegemma:7b')
OLLAMA = os.environ.get('OLLAMA_URL', 'http://localhost:11434/api/generate')
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY') or secrets.token_hex(32)
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax', MAX_CONTENT_LENGTH=2 * 1024 * 1024)
if os.environ.get('COOKIE_SECURE') == '1': app.config['SESSION_COOKIE_SECURE'] = True

def db():
    c = sqlite3.connect(DB, timeout=20)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    return c

def init():
    with db() as c:
        c.executescript('''
        CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL UNIQUE COLLATE NOCASE, password TEXT NOT NULL, creado TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS proyectos (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario_id INTEGER NOT NULL REFERENCES usuarios(id), nombre TEXT NOT NULL, creado TEXT NOT NULL, actualizado TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS versiones (id INTEGER PRIMARY KEY AUTOINCREMENT, proyecto_id INTEGER NOT NULL REFERENCES proyectos(id) ON DELETE CASCADE, numero INTEGER NOT NULL, peticion TEXT NOT NULL, codigo TEXT NOT NULL, creado TEXT NOT NULL, UNIQUE(proyecto_id,numero));
        CREATE INDEX IF NOT EXISTS idx_proyectos_usuario ON proyectos(usuario_id);
        CREATE INDEX IF NOT EXISTS idx_versiones_proyecto ON versiones(proyecto_id,numero);
        CREATE TABLE IF NOT EXISTS generaciones (id INTEGER PRIMARY KEY AUTOINCREMENT, proyecto_id INTEGER NOT NULL, peticion TEXT NOT NULL, estado TEXT NOT NULL, respuesta TEXT NOT NULL DEFAULT '', error TEXT NOT NULL DEFAULT '', creado TEXT NOT NULL, finalizado TEXT);
        CREATE INDEX IF NOT EXISTS idx_generaciones_proyecto ON generaciones(proyecto_id,id);
        ''')
init()

def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')
def logged(fn):
    @wraps(fn)
    def wrapper(*a, **kw):
        if not session.get('uid'): return redirect(url_for('login'))
        return fn(*a, **kw)
    return wrapper

def csrf():
    if 'csrf' not in session: session['csrf'] = secrets.token_urlsafe(32)
    return session['csrf']
app.jinja_env.globals['csrf'] = csrf
@app.before_request
def protect():
    if request.method == 'POST' and not secrets.compare_digest(request.form.get('csrf', ''), csrf()): abort(400, 'Token CSRF inválido')

def project_or_404(c, pid):
    p = c.execute('SELECT * FROM proyectos WHERE id=? AND usuario_id=?', (pid, session['uid'])).fetchone()
    if p is None: abort(404)
    return p

@app.route('/registro', methods=['GET','POST'])
def registro():
    if request.method == 'POST':
        name = request.form.get('nombre','').strip()
        password = request.form.get('password','')
        if not re.fullmatch(r'[\w.-]{3,40}', name, re.UNICODE) or len(password)<8:
            flash('Usuario de 3 a 40 caracteres y contraseña de al menos 8 caracteres.', 'error')
        else:
            try:
                with db() as c:
                    cur=c.execute('INSERT INTO usuarios(nombre,password,creado) VALUES(?,?,?)',(name,generate_password_hash(password),now()))
                    uid=cur.lastrowid
                session.clear(); session['uid']=uid; csrf()
                return redirect(url_for('index'))
            except sqlite3.IntegrityError: flash('El nombre de usuario ya existe.', 'error')
    return render_template('auth.html', title='Crear cuenta', action='registro')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        with db() as c: user=c.execute('SELECT * FROM usuarios WHERE nombre=?',(request.form.get('nombre','').strip(),)).fetchone()
        if user and check_password_hash(user['password'],request.form.get('password','')):
            session.clear(); session['uid']=user['id']; csrf(); return redirect(url_for('index'))
        flash('Credenciales incorrectas.', 'error')
    return render_template('auth.html',title='Iniciar sesión',action='login')

@app.post('/salir')
def salir(): session.clear(); return redirect(url_for('login'))

@app.get('/')
@logged
def index():
    with db() as c:
        projects=c.execute('SELECT p.*, (SELECT MAX(numero) FROM versiones WHERE proyecto_id=p.id) AS ultima FROM proyectos p WHERE usuario_id=? ORDER BY actualizado DESC',(session['uid'],)).fetchall()
        user=c.execute('SELECT nombre FROM usuarios WHERE id=?',(session['uid'],)).fetchone()
    return render_template('index.html', projects=projects, user=user)

@app.post('/proyectos')
@logged
def create():
    name=request.form.get('nombre','').strip()[:100]
    if not name: flash('Introduce un nombre.', 'error'); return redirect(url_for('index'))
    with db() as c:
        cur=c.execute('INSERT INTO proyectos(usuario_id,nombre,creado,actualizado) VALUES(?,?,?,?)',(session['uid'],name,now(),now()))
        pid=cur.lastrowid
    return redirect(url_for('project',pid=pid))

@app.get('/proyectos/<int:pid>')
@logged
def project(pid):
    with db() as c:
        p=project_or_404(c,pid)
        versions=c.execute('SELECT id,numero,peticion,creado FROM versiones WHERE proyecto_id=? ORDER BY numero DESC',(pid,)).fetchall()
        current=c.execute('SELECT * FROM versiones WHERE proyecto_id=? ORDER BY numero DESC LIMIT 1',(pid,)).fetchone()
    return render_template('project.html',p=p,versions=versions,current=current)

@app.post('/proyectos/<int:pid>/generar')
@logged
def generate(pid):
    prompt=request.form.get('peticion','').strip()
    if not prompt or len(prompt)>5000: flash('Petición vacía o demasiado larga (máximo 5000 caracteres).','error'); return redirect(url_for('project',pid=pid))
    with db() as c:
        p=project_or_404(c,pid)
        old=c.execute('SELECT codigo FROM versiones WHERE proyecto_id=? ORDER BY numero DESC LIMIT 1',(pid,)).fetchone()
    instructions=('Eres un desarrollador web. Devuelve SOLO un documento HTML completo, con CSS y JavaScript embebidos, sin markdown ni explicaciones. '
                  'Respeta las funcionalidades existentes al modificar. No uses recursos externos salvo que el usuario lo solicite.\n')
    if old: instructions += '\nCÓDIGO ACTUAL:\n'+old['codigo'][:50000]+'\n\nMODIFICACIÓN SOLICITADA:\n'+prompt
    else: instructions += '\nWEB SOLICITADA:\n'+prompt
    try:
        r=requests.post(OLLAMA,json={'model':MODEL,'prompt':instructions,'stream':False},timeout=180)
        r.raise_for_status()
        code=r.json()['response'].strip()
        code=re.sub(r'^```(?:html)?\s*|\s*```$', '', code, flags=re.I).strip()
        if not code or '<' not in code: raise ValueError('La IA no devolvió HTML válido.')
    except (requests.RequestException,ValueError,KeyError) as e:
        flash(f'Error al generar: {e}', 'error'); return redirect(url_for('project',pid=pid))
    with db() as c:
        project_or_404(c,pid)
        number=c.execute('SELECT COALESCE(MAX(numero),0)+1 FROM versiones WHERE proyecto_id=?',(pid,)).fetchone()[0]
        c.execute('INSERT INTO versiones(proyecto_id,numero,peticion,codigo,creado) VALUES(?,?,?,?,?)',(pid,number,prompt,code,now()))
        c.execute('UPDATE proyectos SET actualizado=? WHERE id=?',(now(),pid))
    return redirect(url_for('project',pid=pid))

def clean_html(raw):
    raw = re.sub(r'```(?:html)?\s*', '', raw, flags=re.I).replace('```', '').strip()
    start = re.search(r'<!doctype\s+html|<html\b', raw, flags=re.I)
    if start: raw = raw[start.start():]
    end = re.search(r'</html\s*>', raw, flags=re.I)
    if end: raw = raw[:end.end()]
    return raw.strip()

@app.post('/proyectos/<int:pid>/generar-stream')
@logged
def generate_stream(pid):
    prompt = request.form.get('peticion', '').strip()
    if not prompt or len(prompt)>5000: abort(400, 'Petición inválida')
    with db() as c:
        project_or_404(c,pid)
        old = c.execute('SELECT codigo FROM versiones WHERE proyecto_id=? ORDER BY numero DESC LIMIT 1',(pid,)).fetchone()
    with db() as c:
        history = c.execute('SELECT numero,peticion FROM versiones WHERE proyecto_id=? ORDER BY numero DESC LIMIT 12',(pid,)).fetchall()
        attempt = c.execute('INSERT INTO generaciones(proyecto_id,peticion,estado,creado) VALUES(?,?,?,?)',(pid,prompt,'iniciada',now())).lastrowid
    history_text = '\n'.join(f"Versión {v['numero']}: {v['peticion']}" for v in reversed(history))
    context = ("Conserva las funciones existentes salvo petición expresa. "
               "El historial describe decisiones anteriores del proyecto; respétalas cuando no contradigan la última solicitud.\n"
               "HISTORIAL DE PETICIONES:\n" + history_text + "\n")
    if old:
        context += '\nCÓDIGO ACTUAL (fuente principal de verdad):\n'+old['codigo']+'\nMODIFICACIÓN SOLICITADA:\n'+prompt
    else:
        context += '\nWEB SOLICITADA:\n'+prompt
    html_instructions = ("Eres un desarrollador web. FASE 1 DE 2: devuelve SOLO un documento HTML completo "
                         "(<!doctype html> hasta </html>), sin markdown ni explicaciones. "
                         "Construye toda la estructura, contenido y comportamiento JavaScript necesario. "
                         "NO escribas CSS: no incluyas <style>, atributos style= ni enlaces a hojas CSS. "
                         "Usa clases e IDs semánticos para que una segunda fase pueda diseñar la página. "
                         "El documento debe ser válido por sí mismo y mantener funcionalidades existentes.\n" + context)
    def event(kind, **kwargs):
        return 'data: '+json.dumps({'type':kind, **kwargs},ensure_ascii=False)+'\n\n'
    def stream():
        fragments=[]; css_fragments=[]; stats={'tokens':0}; complete=False
        try:
            options={'num_ctx':int(os.environ.get('OLLAMA_NUM_CTX','16384'))}
            def ollama_stream(instructions, phase, target):
                nonlocal stats
                with requests.post(OLLAMA,json={'model':MODEL,'prompt':instructions,'stream':True,'options':options},stream=True,timeout=(15,600)) as r:
                    r.raise_for_status()
                    finished=False
                    for line in r.iter_lines():
                        if not line: continue
                        item=json.loads(line)
                        if item.get('error'): raise ValueError(item['error'])
                        chunk=item.get('response','')
                        if chunk:
                            target.append(chunk)
                            yield event('chunk',text=chunk,phase=phase)
                        if item.get('done'):
                            stats['tokens']+=item.get('eval_count',0)
                            finished=True
                            break
                    if not finished: raise ValueError('Ollama interrumpió la fase '+phase)
            yield event('phase',phase='html')
            yield from ollama_stream(html_instructions,'html',fragments)
            html=clean_html(''.join(fragments))
            if not (re.search(r'<html\b',html,re.I) and re.search(r'</html\s*>',html,re.I)):
                raise ValueError('La fase HTML no devolvió un documento completo')
            css_instructions=("Eres un diseñador CSS. FASE 2 DE 2. Devuelve EXCLUSIVAMENTE reglas CSS en texto plano, "
                              "sin markdown, sin etiquetas <style>, sin HTML, sin explicaciones. "
                              "Diseña profesionalmente la siguiente página usando sus clases e IDs existentes. "
                              "No alteres su estructura ni inventes selectores innecesarios. "
                              "Hazla responsive, accesible y visualmente cuidada.\n"
                              "PETICIÓN ORIGINAL:\n"+prompt+"\nHTML GENERADO:\n"+html)
            yield event('phase',phase='css')
            yield from ollama_stream(css_instructions,'css',css_fragments)
            css=''.join(css_fragments).strip()
            css=re.sub(r'^```(?:css)?\s*|\s*```$', '', css, flags=re.I).strip()
            css=re.sub(r'</?style\b[^>]*>', '', css, flags=re.I).strip()
            if not css: raise ValueError('La fase CSS no devolvió estilos')
            # El CSS queda al final del cuerpo, antes de los cierres del documento.
            # Evita insertar CSS después de </html>, lo que produciría HTML inválido.
            style='\n<style id="amable-generated-css">\n'+css+'\n</style>\n'
            if re.search(r'</body\s*>',html,re.I):
                code=re.sub(r'</body\s*>',lambda m:style+m.group(0),html,count=1,flags=re.I)
            else:
                code=re.sub(r'</html\s*>',lambda m:style+m.group(0),html,count=1,flags=re.I)
            complete=True
            with db() as c:
                c.execute('UPDATE generaciones SET respuesta=?,estado=?,error=?,finalizado=? WHERE id=?',
                          (code,'completada','',now(),attempt))
                number=c.execute('SELECT COALESCE(MAX(numero),0)+1 FROM versiones WHERE proyecto_id=?',(pid,)).fetchone()[0]
                cur=c.execute('INSERT INTO versiones(proyecto_id,numero,peticion,codigo,creado) VALUES(?,?,?,?,?)',(pid,number,prompt,code,now()))
                c.execute('UPDATE proyectos SET actualizado=? WHERE id=?',(now(),pid))
                vid=cur.lastrowid
            yield event('done',id=vid,number=number,html=code,**stats)
        except Exception as exc:
            try:
                with db() as c:
                    c.execute('UPDATE generaciones SET respuesta=?,estado=?,error=?,finalizado=? WHERE id=?',
                              (''.join(fragments)+'\n/* CSS PARCIAL */\n'+''.join(css_fragments),'error',str(exc),now(),attempt))
            except sqlite3.Error:
                app.logger.exception('No se pudo registrar el fallo de generación')
            yield event('error',message=str(exc))
    return Response(stream(),mimetype='text/event-stream',headers={'Cache-Control':'no-cache, no-transform','X-Accel-Buffering':'no','X-Content-Type-Options':'nosniff'})

@app.get('/proyectos/<int:pid>/versiones/<int:vid>/codigo')
@logged
def code(pid,vid):
    with db() as c:
        project_or_404(c,pid)
        v=c.execute('SELECT codigo FROM versiones WHERE id=? AND proyecto_id=?',(vid,pid)).fetchone()
    if not v: abort(404)
    return Response(v['codigo'],content_type='text/plain; charset=utf-8',headers={'Cache-Control':'no-store','X-Content-Type-Options':'nosniff'})

@app.get('/proyectos/<int:pid>/versiones/<int:vid>/descargar')
@logged
def download(pid,vid):
    with db() as c:
        project_or_404(c,pid)
        v=c.execute('SELECT codigo FROM versiones WHERE id=? AND proyecto_id=?',(vid,pid)).fetchone()
    if not v: abort(404)
    return Response(v['codigo'],content_type='application/octet-stream',headers={'Content-Disposition':f'attachment; filename="proyecto-{pid}-version-{vid}.html"','X-Content-Type-Options':'nosniff'})

@app.post('/proyectos/<int:pid>/restaurar/<int:vid>')
@logged
def restore(pid,vid):
    with db() as c:
        project_or_404(c,pid)
        v=c.execute('SELECT codigo,numero FROM versiones WHERE id=? AND proyecto_id=?',(vid,pid)).fetchone()
        if not v: abort(404)
        number=c.execute('SELECT COALESCE(MAX(numero),0)+1 FROM versiones WHERE proyecto_id=?',(pid,)).fetchone()[0]
        c.execute('INSERT INTO versiones(proyecto_id,numero,peticion,codigo,creado) VALUES(?,?,?,?,?)',(pid,number,f'Restauración de la versión {v["numero"]}',v['codigo'],now()))
        c.execute('UPDATE proyectos SET actualizado=? WHERE id=?',(now(),pid))
    return redirect(url_for('project',pid=pid))

@app.post('/proyectos/<int:pid>/renombrar')
@logged
def rename(pid):
    name=request.form.get('nombre','').strip()[:100]
    with db() as c:
        project_or_404(c,pid)
        if name: c.execute('UPDATE proyectos SET nombre=?,actualizado=? WHERE id=?',(name,now(),pid))
    return redirect(url_for('project',pid=pid))

@app.post('/proyectos/<int:pid>/eliminar')
@logged
def delete(pid):
    with db() as c:
        project_or_404(c,pid)
        c.execute('DELETE FROM versiones WHERE proyecto_id=?',(pid,))
        c.execute('DELETE FROM proyectos WHERE id=?',(pid,))
    return redirect(url_for('index'))

if __name__ == '__main__': app.run(debug=False)
