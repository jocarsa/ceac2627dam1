# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template,request

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("frente.html")

@aplicacion.route("/tabla")
def tabla():
  return render_template("tabla.html")

@aplicacion.route("/formulario")
def formulario():
  return render_template("formulario.html")

@aplicacion.route("/inserta",methods=['POST'])
def inserta():
  return render_template("inserta.html")

if __name__ == "__main__":
  aplicacion.run()