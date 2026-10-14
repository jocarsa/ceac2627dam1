# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='blogceac2627',
  password='CEAC123$',
  database='blogceac2627'
)
# Compruebo si la conexión es correcta
if connection.is_connected():
  print("Todo ha ido bien")
else:
  print("Ha habido un error")
  
connection.close()
