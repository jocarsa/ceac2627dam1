# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='blogceac2627',
  password='CEAC123$',
  database='blogceac2627'
)

  
connection.close()
