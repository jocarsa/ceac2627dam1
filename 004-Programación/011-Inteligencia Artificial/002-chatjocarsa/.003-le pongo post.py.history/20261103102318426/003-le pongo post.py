# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template

aplicacion = Flask("__name__") 

# Escucho en la raiz
@aplicacion.route("/")
def inicio():
  return render_template("chat.html")

@aplicacion.route("/pregunta",methods=['POST'])
def pregunta():
  print(reques.form['pregunta'])
  return render_template("respuesta.html")


if __name__ == "__main__":
  aplicacion.run()