# Primero importo la librería de conexión
import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='programacion2627',
  password='TAME123$',
  database='programacion2627'
)
if connection.is_connected():
  print("Connected to MySQL database")
  
connection.close()
