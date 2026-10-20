from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/procesa")
def procesa():
  return "ok yo te voy a procesar el formulario"
  
if __name__ == "__main__":
  aplicacion.run()