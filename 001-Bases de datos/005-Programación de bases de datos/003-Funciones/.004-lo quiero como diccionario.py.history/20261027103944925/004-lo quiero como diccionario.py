import sqlite3

conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor(dict=True)

cursor.execute("SELECT * FROM clientes")

resultados = cursor.fetchall()
print(resultados)

conexion.close()