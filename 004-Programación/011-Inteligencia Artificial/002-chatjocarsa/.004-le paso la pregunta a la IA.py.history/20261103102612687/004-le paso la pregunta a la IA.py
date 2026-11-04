# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template,request
import requests

aplicacion = Flask("__name__") 

# Escucho en la raiz
@aplicacion.route("/")
def inicio():
  return render_template("chat.html")

@aplicacion.route("/pregunta",methods=['POST'])
def pregunta():
  # Defino la ruta donde ollama está escuchando (esto es fijo)
  ruta = "http://localhost:11434/api/generate"
  # Elijo un modelo de entre los que he descargado
  modelo = "phi4-mini"
  # Establezco una pregunta
  pregunta = request.form['pregunta'] # Es la pregunta que viene del formulario
  # Elijo si me suelta la respuesta de golpe o palabra a palabra
  flujo = False
  # Hago una petición a la red (local!!!!)
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })

  print(str(r.json()["response"]))
  return render_template("respuesta.html")


if __name__ == "__main__":
  aplicacion.run()