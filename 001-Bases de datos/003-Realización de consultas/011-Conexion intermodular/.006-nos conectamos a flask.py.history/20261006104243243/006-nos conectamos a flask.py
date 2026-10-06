# Primero importo las librerías
import mysql.connector # Primero importo MySQL
from flask import Flask # Y también importo Flask

# Me conecto con las credenciales correctas
connection = mysql.connector.connect(
  host='localhost',
  user='tiendaestetoscopios',
  password='TiendaEstetoscopios123$',
  database='tiendaestetoscopios'
)

# Creo un cursor
cursor = connection.cursor()

# Ahora creo una aplicación base
aplicacion = Flask("__name__") 

# Defino un punto donde flask va a escuchar en la web
@aplicacion.route("/")
def inicio():
  cadena = ""
  # Ejecuto una petición a la base de datos
  cursor.execute("SELECT * FROM estetoscopios")	

  # Recupero el resultado de la petición
  filas = cursor.fetchall()	

  # Recorro el resultado y lo pinto en pantalla
  for fila in filas:
    print(fila)
  
# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run()

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
