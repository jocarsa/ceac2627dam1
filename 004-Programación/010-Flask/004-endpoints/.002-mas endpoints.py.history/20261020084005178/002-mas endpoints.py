from flask import Flask

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return "yo soy la pagina de inicio"

@aplicacion.route("/sobremi")
def inicio():
  return "yo soy la pagina de sobre mi"

@aplicacion.route("/proyectos")
def inicio():
  return "esta es la página de mis proyectos"

@aplicacion.route("/contacto")
def inicio():
  return "esta es la página de contacto"


if __name__ == "__main__":
  aplicacion.run()