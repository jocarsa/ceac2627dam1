import sqlite3

conexion = sqlite3.connect("empresa.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()

cursor.execute("SELECT * FROM clientes")

resultados = [dict(fila) for fila in cursor.fetchall()]
print(resultados)

conexion.close()