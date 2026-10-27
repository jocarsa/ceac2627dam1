import sqlite3

conexion = sqlite3.connect("empresa.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM clientes")

resultados = cursor.fetchall()
print(resultados)

conexion.close()