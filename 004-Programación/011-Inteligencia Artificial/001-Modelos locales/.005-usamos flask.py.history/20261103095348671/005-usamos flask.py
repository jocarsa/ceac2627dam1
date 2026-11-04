# Importo la librería de crear páginas web
from flask import Flask, render_template
import requests

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  # Defino la ruta donde ollama está escuchando (esto es fijo)
  ruta = "http://localhost:11434/api/generate"
  # Elijo un modelo de entre los que he descargado
  modelo = "qwen3.5:0.8b"
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
  return r.json()["response"]

  
if __name__ == "__main__":
  aplicacion.run()