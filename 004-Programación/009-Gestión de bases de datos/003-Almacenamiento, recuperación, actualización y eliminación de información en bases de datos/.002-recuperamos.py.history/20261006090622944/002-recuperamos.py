import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM calzados")	

filas = cursor.fetchall()	

# Devuelvo las filas
for fila in filas:
  print(fila)

cursor.close()
connection.close()
