import os

directorio = "/var/www/html/ceac2627dam1"

for raiz, carpetas, archivos in os.walk(directorio):

    # Calcular nivel de profundidad
    nivel = raiz.replace(directorio, "").count(os.sep)

    # Mostrar carpeta actual
    indentacion = "    " * nivel
    print(indentacion + "📁 " + os.path.basename(raiz) + "/")

    # Mostrar archivos
    indentacion_archivos = "    " * (nivel + 1)

    for archivo in archivos:
        print(indentacion_archivos + "📄 " + archivo)