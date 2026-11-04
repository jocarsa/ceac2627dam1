# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template

aplicacion = Flask("__name__") 

# Escucho en la raiz
@aplicacion.route("/pregunta")
def pregunta():
  return render_template("respuesta.html")

@aplicacion.route("/")
if __name__ == "__main__":
  aplicacion.run()