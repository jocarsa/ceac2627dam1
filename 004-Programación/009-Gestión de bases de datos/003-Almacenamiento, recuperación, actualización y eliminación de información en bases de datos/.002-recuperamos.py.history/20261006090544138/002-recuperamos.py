import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)

cursor = connection.cursor()



cursor.close()
connection.close()
