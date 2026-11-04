from flask import Flask,render_template,request		# Para la web
import requests																		# Para hacer peticiones http

aplicacion = Flask("__name__") 										# Creamos una aplicacion


@aplicacion.route("/")														# Escucho en la raiz
def inicio():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "qwen2.5-coder:0.5b"										# Elijo el modelo
  pregunta = """
  	create an html web page
    give me only the code
    """ 																					# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  return render_template("chat.html")

@aplicacion.route("/pregunta",methods=['POST'])
def pregunta():
  # Defino la ruta donde ollama está escuchando (esto es fijo)
  
  # Elijo un modelo de entre los que he descargado
  
  # Establezco una pregunta
  
  # Elijo si me suelta la respuesta de golpe o palabra a palabra
  
  # Hago una petición a la red (local!!!!)
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })

  mirespuesta = str(r.json()["response"])
  # Llamo a la plantilla y le paso la respuesta
  return render_template("respuesta.html",respuesta=mirespuesta)


if __name__ == "__main__":
  aplicacion.run()