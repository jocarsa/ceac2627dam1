import sqlite3

conexion = sqlite3.connect("blog.db")
conexion.row_factory = sqlite3.Row

cursor = conexion.cursor()
cursor.execute("SELECT * FROM clientes")

for fila in cursor.fetchall():
    print(dict(fila))

conexion.close()