from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("inicio.html")

@aplicacion.route("/sobremi")
def sobremi():
  return "yo soy la pagina de sobre mi"

@aplicacion.route("/proyectos")
def proyectos():
  return "esta es la página de mis proyectos"

@aplicacion.route("/contacto")
def contacto():
  return "esta es la página de contacto"

#...


if __name__ == "__main__":
  aplicacion.run()