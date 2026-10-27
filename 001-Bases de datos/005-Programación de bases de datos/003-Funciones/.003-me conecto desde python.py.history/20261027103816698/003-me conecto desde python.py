import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("basedatos.db")

# Crear cursor
cursor = conexion.cursor()

# Ejecutar SELECT
cursor.execute("SELECT * FROM alumnos")

# Obtener resultados
resultados = cursor.fetchall()

# Mostrar resultados
for fila in resultados:
    print(fila)

# Cerrar conexión
conexion.close()