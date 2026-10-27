# CMS mejorado

Mantiene la tabla MySQL `articulos` existente y las rutas originales `/`, `/tabla`, `/formulario`, `/inserta`.

Instalación:

```bash
pip install flask mysql-connector-python
python3 '004-conectamos con mysql.py'
```

Configura `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` y `FLASK_SECRET_KEY` mediante variables de entorno cuando lo despliegues. El archivo conserva los valores de conexión de la práctica para uso local.

**Importante:** el panel de administración no incluye autenticación (igual que el ejercicio original). No debe publicarse en Internet sin proteger las rutas de creación, edición y eliminación, añadir CSRF y desactivar debug.
