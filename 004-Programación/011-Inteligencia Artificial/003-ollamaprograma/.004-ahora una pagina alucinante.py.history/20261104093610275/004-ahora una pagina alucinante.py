from flask import Flask	# Para la web
import requests																		# Para hacer peticiones http

aplicacion = Flask("__name__") 										# Creamos una aplicacion


@aplicacion.route("/")														# Escucho en la raiz
def inicio():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "qwen2.5-coder:3b"										# Elijo el modelo
  pregunta = """
  	-create an amazing html web page with css
    -add fancy css style
    -give me only the code, no comments, no fences, no markdown, only html and css
    -the web will be about the person Jose Vicente Carratala
    -use clear colors
    """ 																					# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																							# Ejecutamos la petición
  mirespuesta = str(r.json()["response"])					# Obtenemos la respuesta
  return mirespuesta															# Lo que sea que venga, lo pinto en html

if __name__ == "__main__":
  aplicacion.run()