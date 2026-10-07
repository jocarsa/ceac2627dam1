from flask import Flask

aplicacion = Flask("__name__") # creamos una nueva aplicación

@aplicacion.route("/")
def inicio():
  