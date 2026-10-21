from flask import Flask,render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos")
def sobremi():
  return "yo voy a recoger tus datos"



if __name__ == "__main__":
  aplicacion.run()