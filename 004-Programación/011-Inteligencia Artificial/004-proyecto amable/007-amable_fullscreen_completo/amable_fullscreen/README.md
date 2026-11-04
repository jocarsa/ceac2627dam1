# Amable — vista navegador completo

## Instalación

1. Descomprime el proyecto.
2. Si ya usas Amable, **copia tu `amable.db` actual** a esta carpeta (no se incluye ninguna base de datos para evitar sobrescribir tus datos).
3. Instala dependencias: `pip install -r requirements.txt`.
4. Ejecuta: `python3 app.py`.
5. Abre http://127.0.0.1:5000

Configuración opcional: `OLLAMA_MODEL=qwen2.5-coder:7b OLLAMA_NUM_CTX=16384 python3 app.py`.

## Novedades

- Vista previa a pantalla completa, sin barras laterales fijas.
- Barra de herramientas flotante compacta.
- Paneles de historial, código y ajustes desplegables.
- Compositor de prompts translúcido, arrastrable, ocultable, con posición guardada localmente.
- Streaming de HTML al panel de código y a la vista previa.
- Registro de generaciones y versiones en SQLite; historial de instrucciones anteriores.
- Exportación HTML y restauración de versiones.

## Seguridad y límites

El iframe de vista previa usa `sandbox="allow-scripts"` sin `allow-same-origin`, para aislar los scripts generados. No se recomienda publicar el servidor de desarrollo de Flask directamente en Internet. Usa `SECRET_KEY` estable y HTTPS en producción. Las vistas previas pueden reiniciar scripts durante el streaming. Una generación incompleta queda registrada en `generaciones` pero no reemplaza una versión válida.
