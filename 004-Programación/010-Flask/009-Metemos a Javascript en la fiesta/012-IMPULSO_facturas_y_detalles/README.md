# IMPULSO — Tienda deportiva + Administración

Basada en el proyecto Flask/SQLite «009-Metemos a Javascript en la fiesta».

## Instalar

```bash
cd tienda_deportiva_pro
python3 -m pip install flask
export ADMIN_PASSWORD='pon-aqui-una-contrasena-larga'
export SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_hex(32))')"
python3 app.py
```

- Tienda: http://127.0.0.1:5000/
- Administración: http://127.0.0.1:5000/admin

## Conservar tus datos

Copia tu `tienda.db` original junto a `app.py` ANTES de arrancar. El programa reutiliza las tablas `productos` y `pedidos` y crea `pedido_estados` automáticamente. Si no existe base de datos, crea una con productos de ejemplo.

Los pedidos antiguos almacenados en `carga` se muestran cuando el JSON contiene una lista de artículos con nombre y precio.

El administrador se autentica mediante ADMIN_PASSWORD o ADMIN_PASSWORD_HASH. No hay contraseña predeterminada. No uses el servidor de desarrollo Flask con `debug=True` en producción; despliega detrás de HTTPS y un servidor WSGI. Esta aplicación es una demo de pedidos, no incluye pasarela de pago.
