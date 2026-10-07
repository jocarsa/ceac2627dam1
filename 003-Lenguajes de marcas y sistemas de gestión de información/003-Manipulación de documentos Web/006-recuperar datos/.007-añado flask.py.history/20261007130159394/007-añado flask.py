# Primero importo la librería
import mysql.connector
from flask import Flask

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='encuentrame',
  password='Encuentrame123$',
  database='encuentrame'
)

# Creo un cursor
cursor = connection.cursor()

aplicacion = Flask("__name__")

# Ejecuto una petición a la base de datos
cursor.execute("SELECT * FROM facultativos")	

# Recupero el resultado de la petición
filas = cursor.fetchall()	

# Recorro el resultado y lo pinto en pantalla
for fila in filas:
  print(fila)

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
