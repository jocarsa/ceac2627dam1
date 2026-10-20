# Importo Flask para la web y connector para MySQL
from flask import Flask, render_template, request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='caminodeida',
        password='CEAC123$',
        database='caminodeida'
    )

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/procesa", methods=["POST"])
def procesa():
  ######################### MYSQL
 	# Creo un cursor para poder pedir cosas
  cursor = connection.cursor()

  # Ejecuto una petición sobre el cursor
  cursor.execute("""
        INSERT INTO clientes (nombre, apellidos, email)
        VALUES (%s, %s, %s);
    """, (
        request.form["titulo"],
        request.form["fecha"],
        request.form["texto"]
    ))

  connection.commit()
  # Ahora atrapo los parametros
  cadena = ""
  cadena += request.form["nombre"]
  cadena += request.form["apellidos"]
  cadena += request.form["email"]
  return "ok yo te voy a procesar el formulario: "+cadena 
  
if __name__ == "__main__":
  aplicacion.run()