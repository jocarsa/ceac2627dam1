from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return "yo soy la pagina de inicio"

@aplicacion.route("/sobremi")
def sobremi():
  return "yo soy la pagina de sobre mi"



if __name__ == "__main__":
  aplicacion.run()