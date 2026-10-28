from flask import Flask,render_template	# Importo flask para crear una web
import json	# Importo json para poder enviar json
import sqlite3	# Import sqlite3 para poder conectarme a una base de datos

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

@aplicacion.route("/datos")
def datos():
    conexion = sqlite3.connect("tienda.db") # Me conecto a la base de datos
    conexion.row_factory = sqlite3.Row # Lo que venga lo quiero como diccionario
    cursor = conexion.cursor() # Creo un cursor necesario
    cursor.execute("SELECT * FROM productos") # Le pido los artículos
    articulos = cursor.fetchall() # Cargo los artículos en una variable

    # Cierro la conexión
    conexion.close()

    # Pinto la plantilla
    return render_template("frente.html", datos=articulos)

if __name__ == "__main__":
  aplicacion.run()