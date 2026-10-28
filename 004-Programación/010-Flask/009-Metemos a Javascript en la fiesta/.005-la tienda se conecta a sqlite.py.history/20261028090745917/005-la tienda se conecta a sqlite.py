from flask import Flask,render_template
import json
import sqlite3

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

@aplicacion.route("/datos")
def datos():
  return 

if __name__ == "__main__":
  aplicacion.run()