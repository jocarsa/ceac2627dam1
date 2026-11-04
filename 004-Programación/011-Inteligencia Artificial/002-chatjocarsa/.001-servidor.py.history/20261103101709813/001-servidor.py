# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("frente.html")

@aplicacion.route("/datos")
def datos():
  return "ok"


if __name__ == "__main__":
  aplicacion.run()