# Primero importo la librería de conexión y la libreria web
import mysql.connector
from flask import Flask, render_template

# Me conecto a la base de datos, pero usando los datos que acabamos de crear
connection = mysql.connector.connect(
  host='localhost',
  user='curriculum',
  password='CEAC123$',
  database='curriculum'
)

# creo una aplicación web
aplicacion = Flask("__name__") 


@aplicacion.route("/")
def inicio():
  # Creo un cursor
  cursor = connection.cursor(dictionary=True)

  # Ejecuto una petición a la base de datos
  cursor.execute("SELECT * FROM articulos")	

  # Recupero el resultado de la petición
  filas = cursor.fetchall()	

  return render_template(
    	"blog.html",
    	titulo = "El blog de Jose Vicente",
    	subtitulo = "Esto es un blog",
    	articulos = filas
  )

if __name__ == "__main__":
  aplicacion.run()
connection.close()
