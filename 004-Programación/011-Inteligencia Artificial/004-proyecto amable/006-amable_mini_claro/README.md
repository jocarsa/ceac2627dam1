# Amable mini

Aplicación Flask + SQLite + Ollama con usuarios, proyectos, versiones, restauración y vista previa.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ollama pull qwen2.5-coder:3b
export SECRET_KEY="$(python3 -c 'import secrets;print(secrets.token_hex(32))')"
python app.py
```

Abrir http://127.0.0.1:5000 y registrarse.

Opcional: `OLLAMA_MODEL`, `OLLAMA_URL`, `AMABLE_DB`, `COOKIE_SECURE=1` (con HTTPS).

Si copias tu `amable.db` anterior a esta carpeta antes de iniciar, se conservará la tabla `webs`. Los registros históricos antiguos no se asignan automáticamente a usuarios, porque no existe una relación fiable con sus cuentas.

Para un despliegue público: HTTPS, SECRET_KEY persistente, servidor WSGI, limitación de peticiones y cuotas de generación. El HTML generado es código no confiable: la vista previa usa un iframe sandbox, pero no debe ejecutarse en el servidor.
