# Importo request para enviar datos
from flask import Flask, render_template, request

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/procesa", methods=["POST"])
def procesa():
  # Ahora atrapo los parametros
  cadena = ""
  cadena += request.form["nombre"]
  cadena += request.form["apellidos"]
  cadena += request.form["email"]
  return "ok yo te voy a procesar el formulario: "+cadena 
  
if __name__ == "__main__":
  aplicacion.run()