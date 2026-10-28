import os,sqlite3,json,secrets
from datetime import datetime
from decimal import Decimal
from functools import wraps
from flask import Flask,render_template,request,jsonify,session,redirect,url_for
from werkzeug.security import check_password_hash,generate_password_hash

BASE=os.path.dirname(os.path.abspath(__file__))
DB=os.path.join(BASE,'tienda.db')
app=Flask(__name__)
app.secret_key=os.environ.get('SECRET_KEY',secrets.token_hex(32))
app.config.update(SESSION_COOKIE_HTTPONLY=True,SESSION_COOKIE_SAMESITE='Lax')

def db():
 c=sqlite3.connect(DB);c.row_factory=sqlite3.Row;return c

def init():
 with db() as c:
  c.execute('CREATE TABLE IF NOT EXISTS productos (id INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT,descripcion TEXT,precio TEXT)')
  c.execute('CREATE TABLE IF NOT EXISTS pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT,numerodepedido TEXT,fecha TEXT,carga TEXT)')
  c.execute('CREATE TABLE IF NOT EXISTS pedido_clientes (pedido_id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellidos TEXT NOT NULL, email TEXT NOT NULL)')
  c.execute('CREATE TABLE IF NOT EXISTS pedido_estados (pedido_id INTEGER PRIMARY KEY,estado TEXT NOT NULL DEFAULT "Pendiente")')
  if not c.execute('SELECT 1 FROM productos LIMIT 1').fetchone():
   items=[('Zapatillas running','Zapatillas ligeras para correr',59),('Zapatillas fútbol','Botas para césped artificial',75),('Zapatillas baloncesto','Amortiguación de alto rendimiento',89),('Camiseta deportiva','Tejido técnico transpirable',19),('Pantalón corto','Ligero y flexible',24),('Sudadera deportiva','Con capucha para entrenar',45),('Chándal completo','Chaqueta y pantalón',69),('Mochila deportiva','Capacidad de 30 litros',39),('Balón de fútbol','Tamaño oficial 5',29),('Raqueta de tenis','Grafito de alta calidad',95),('Pala de pádel','Fibra de carbono',110),('Mancuernas 5 kg','Pareja de mancuernas',39),('Esterilla fitness','Antideslizante',22),('Bicicleta estática','Con pantalla digital',249),('Reloj deportivo','Con pulsómetro',129)]
   c.executemany('INSERT INTO productos(nombre,descripcion,precio) VALUES(?,?,?)',items)
init()

@app.get('/')
def home():return render_template('tienda.html')
@app.get('/datos')
def datos():
 with db() as c:return jsonify([dict(x) for x in c.execute('SELECT * FROM productos ORDER BY id')])
@app.post('/insertapedido')
def insertar():
 payload=request.get_json(silent=True)
 if not isinstance(payload,dict):return jsonify(error='Pedido no válido'),400
 cliente=payload.get('cliente') or {}
 if not isinstance(cliente,dict):return jsonify(error='Datos de cliente incorrectos'),400
 nombre=str(cliente.get('nombre','')).strip();apellidos=str(cliente.get('apellidos','')).strip();email=str(cliente.get('email','')).strip()
 if not nombre or not apellidos or not email or len(nombre)>100 or len(apellidos)>150 or len(email)>254 or '@' not in email or '.' not in email.split('@')[-1]:return jsonify(error='Introduce nombre, apellidos y un email válido'),400
 payload=payload.get('productos')
 if not isinstance(payload,list) or not payload or len(payload)>100:return jsonify(error='Pedido no válido'),400
 cantidades={}
 for item in payload:
  if not isinstance(item,dict):return jsonify(error='Producto no válido'),400
  try: pid=int(item.get('id'));qty=int(item.get('cantidad',1))
  except (ValueError,TypeError):return jsonify(error='Cantidad no válida'),400
  if qty<1 or qty>50:return jsonify(error='Cantidad fuera de rango'),400
  cantidades[pid]=cantidades.get(pid,0)+qty
 if any(q>50 for q in cantidades.values()):return jsonify(error='Cantidad excesiva'),400
 with db() as c:
  productos={x['id']:dict(x) for x in c.execute('SELECT * FROM productos')}
  if any(i not in productos for i in cantidades):return jsonify(error='Producto desconocido'),400
  lineas=[{'id':i,'nombre':productos[i]['nombre'],'precio':str(productos[i]['precio']),'cantidad':q} for i,q in cantidades.items()]
  total=sum(Decimal(x['precio'])*x['cantidad'] for x in lineas)
  fecha=datetime.now().isoformat(timespec='seconds')
  cur=c.execute('INSERT INTO pedidos(numerodepedido,fecha,carga) VALUES(?,?,?)',('',fecha,json.dumps(lineas,ensure_ascii=False)))
  numero=f'PED-{datetime.now():%Y%m%d}-{cur.lastrowid:05d}'
  c.execute('UPDATE pedidos SET numerodepedido=? WHERE id=?',(numero,cur.lastrowid))
  c.execute('INSERT INTO pedido_clientes(pedido_id,nombre,apellidos,email) VALUES(?,?,?,?)',(cur.lastrowid,nombre,apellidos,email))
 return jsonify(ok=True,numero=numero,total=float(total)),201

def protegido(fn):
 @wraps(fn)
 def wrapper(*args,**kwargs):
  if not session.get('admin'):return redirect(url_for('login'))
  return fn(*args,**kwargs)
 return wrapper

@app.route('/admin/login',methods=['GET','POST'])
def login():
 error=None
 if request.method=='POST':
  password="jocarsa"
  hash_=os.environ.get('ADMIN_PASSWORD_HASH')
  if (hash_ and check_password_hash(hash_,request.form.get('password',''))) or (password and secrets.compare_digest(password,request.form.get('password',''))):
   session.clear();session['admin']=True;return redirect(url_for('admin'))
  error='Contraseña incorrecta o ADMIN_PASSWORD no configurada'
 return render_template('login.html',error=error)
@app.post('/admin/logout')
def logout():session.clear();return redirect(url_for('home'))
@app.get('/admin')
@protegido
def admin():return render_template('admin.html')
@app.get('/admin/pedidos')
@protegido
def pedidos():
 with db() as c:
  rows=c.execute('SELECT p.*,cl.nombre,cl.apellidos,cl.email,COALESCE(e.estado,"Pendiente") estado FROM pedidos p LEFT JOIN pedido_estados e ON e.pedido_id=p.id LEFT JOIN pedido_clientes cl ON cl.pedido_id=p.id ORDER BY p.id DESC').fetchall()
 salida=[]
 for r in rows:
  try:
   carga=json.loads(r['carga'] or '[]')
   if not isinstance(carga,list):carga=[]
  except (ValueError,TypeError):carga=[]
  total=sum(float(x.get('precio',0))*int(x.get('cantidad',1)) for x in carga if isinstance(x,dict))
  salida.append(dict(id=r['id'],numero=r['numerodepedido'] or f'#{r["id"]}',fecha=r['fecha'],nombre=r['nombre'] or '',apellidos=r['apellidos'] or '',email=r['email'] or '',estado=r['estado'],lineas=carga,total=round(total,2)))
 return jsonify(salida)
@app.post('/admin/pedidos/<int:id>/estado')
@protegido
def estado(id):
 valor=(request.get_json(silent=True) or {}).get('estado')
 if valor not in ['Pendiente','Preparando','Enviado','Entregado','Cancelado']:return jsonify(error='Estado inválido'),400
 with db() as c:
  if not c.execute('SELECT 1 FROM pedidos WHERE id=?',(id,)).fetchone():return jsonify(error='No encontrado'),404
  c.execute('INSERT INTO pedido_estados(pedido_id,estado) VALUES(?,?) ON CONFLICT(pedido_id) DO UPDATE SET estado=excluded.estado',(id,valor))
 return jsonify(ok=True)
if __name__=='__main__':app.run(debug=True)
