from flask import Flask,render_template	# Importo flask para crear una web
import json	# Importo json para poder enviar json
import sqlite3	# Import sqlite3 para poder conectarme a una base de datos

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

@aplicacion.route("/datos")
def datos():
  return 

if __name__ == "__main__":
  aplicacion.run()