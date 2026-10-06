# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='tiendacalzado',
  password='TiendaCalzado123$',
  database='tiendacalzado'
)
if connection.is_connected():
  print("Connected to MySQL database")
  
connection.close()
