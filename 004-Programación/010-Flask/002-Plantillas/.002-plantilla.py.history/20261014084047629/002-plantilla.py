from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  render_template("index.html")
  
