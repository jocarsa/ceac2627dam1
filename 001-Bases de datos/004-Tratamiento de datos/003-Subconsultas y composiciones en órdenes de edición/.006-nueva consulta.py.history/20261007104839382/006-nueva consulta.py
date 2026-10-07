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
################### PRIMERO PIDO UN CLIENTE ################
cursor.execute("""
	SELECT * FROM clientes
  WHERE nombre = "Laura"
  """)	
filas = cursor.fetchall()	
idcliente = 0
for fila in filas:
  print(fila)
  idcliente = fila[0]
print("el id del cliente es: ",idcliente)

################### AHORA PIDO LOS PEDIDOS ################

cursor.execute("""
	SELECT * FROM pedidos
  WHERE cliente_id = """+idcliente+"""
  """)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
