# Primero importo la librería
import mysql.connector

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='subconsultas',
  password='Subconsultas123$',
  database='subconsultas'
)

# Creo un cursor
cursor = connection.cursor()
################### PRIMERO PIDO UN CLIENTE
# Ejecuto una petición a la base de datos
cursor.execute("""
	SELECT * FROM clientes
  WHERE nombre = "Laura"
  """)	

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
