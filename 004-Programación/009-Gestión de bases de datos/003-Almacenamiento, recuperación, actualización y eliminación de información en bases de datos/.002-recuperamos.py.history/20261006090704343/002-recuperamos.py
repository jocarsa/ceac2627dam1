# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzados'
)

# Creo un cursor
cursor = connection.cursor()

# Ejecuto una petición a la base de datos
cursor.execute("SELECT * FROM calzados")	

filas = cursor.fetchall()	

for fila in filas:
  print(fila)

cursor.close()
connection.close()
