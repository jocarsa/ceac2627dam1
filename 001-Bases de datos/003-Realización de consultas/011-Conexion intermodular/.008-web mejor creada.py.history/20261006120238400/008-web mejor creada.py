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
  # Creo una cadena vacia
  cadena = """
  	<!doctype html>
    <html>
    	<head>
      </head>
      <body>
      <h1>Tienda de estetoscopios</h1>
  """
  # Ejecuto una petición a la base de datos
  cursor.execute("SELECT * FROM estetoscopios")	
  # Recupero el resultado de la petición
  filas = cursor.fetchall()	
  # Recorro el resultado
  for fila in filas:
    cadena += """
    	<article>
      	<h3>"""+fila[1]+"""</h3>
        <p>"""+fila[2]+"""</p>
        <p>"""+str(fila[3])+"""</p>
      </article>
    """
  # Lo devuelvo a HTML
  return cadena
  
# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run()

# Todo lo que se abre se debe cerrar
cursor.close()
connection.close()
