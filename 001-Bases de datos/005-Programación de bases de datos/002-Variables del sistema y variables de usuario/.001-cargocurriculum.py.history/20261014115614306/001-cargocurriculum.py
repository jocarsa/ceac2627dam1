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
	# Datos personales
  cursor.execute("SELECT * FROM datos_personales")	
  fila = cursor.fetchone()	
  nombre = fila['nombre']
  apellidos = fila['apellidos']
  # Redes sociales
  cursor.execute("SELECT * FROM redes_sociales")	
  fila = cursor.fetchone()	
  facebook = fila['facebook']
  linkedin = fila['linkedin']
  github = fila['github']
  instagram = fila['instagram']

  return render_template(
    	"curriculum.html",
    	nombre = nombre,
    	apellidos = apellidos
  )

if __name__ == "__main__":
  aplicacion.run()
connection.close()
