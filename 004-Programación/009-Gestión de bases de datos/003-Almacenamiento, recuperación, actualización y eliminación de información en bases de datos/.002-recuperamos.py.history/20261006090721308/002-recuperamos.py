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

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

cursor.close()
connection.close()
