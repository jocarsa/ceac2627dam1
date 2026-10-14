# Primero importo la librería de conexión
import mysql.connector

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='blogceac2627',
  password='CEAC123$',
  database='blogceac2627'
)

# Creo un cursor
cursor = connection.cursor()

# Ejecuto una petición a la base de datos
cursor.execute("SELECT * FROM articulos")	

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

connection.close()
