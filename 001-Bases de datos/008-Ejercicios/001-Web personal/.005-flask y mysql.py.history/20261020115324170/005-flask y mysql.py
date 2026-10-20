from flask import Flask,render_template
import mysql.connector

aplicacion = Flask("__name__") 

connection = mysql.connector.connect(
  host='localhost',
  user='miweb',
  password='CEAC123$',
  database='miweb'
)

@aplicacion.route("/")
def inicio():
  return render_template("inicio.html")

@aplicacion.route("/sobremi")
def sobremi():
  return render_template("sobremi.html")

@aplicacion.route("/proyectos")
def proyectos():
  return render_template("proyectos.html")

@aplicacion.route("/contacto")
def contacto():
  return render_template("contacto.html")

#...


if __name__ == "__main__":
  aplicacion.run()