# Importo la librería de crear páginas web
from flask import Flask
# Importo la librería de pedir cosas a la red
import requests

# Creo una aplicación web
aplicacion = Flask("__name__") 

# Escucho en la raiz
@aplicacion.route("/")
def inicio():
  # Defino la ruta donde ollama está escuchando (esto es fijo)
  ruta = "http://localhost:11434/api/generate"
  # Elijo un modelo de entre los que he descargado
  modelo = "phi4-mini"
  # Establezco una pregunta
  pregunta = "Hola quien eres?"
  # Elijo si me suelta la respuesta de golpe o palabra a palabra
  flujo = False
  # Hago una petición a la red (local!!!!)
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })
  # Imprime la respuesta
  return str(r.json()["response"])

  
if __name__ == "__main__":
  aplicacion.run()