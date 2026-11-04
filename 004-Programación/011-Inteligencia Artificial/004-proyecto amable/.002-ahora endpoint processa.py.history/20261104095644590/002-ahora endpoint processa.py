from flask import Flask,render_template,request				# En primer lugar importo la librería

aplicacion = Flask("__name__") 								# Ahora creo una aplicación base

@aplicacion.route("/")												# Defino un punto donde flask va a escuchar en la web
def inicio():
  return render_template("principal.html")

@aplicacion.route("/procesa",methods=['POST'])
def procesa():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "qwen2.5-coder:3b"											# Elijo el modelo
  pregunta = reques.form['peticion']							# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																							# Ejecutamos la petición
  mirespuesta = str(r.json()["response"])					# Obtenemos la respuesta
  return mirespuesta															# Lo que sea que venga, lo pinto en html

if __name__ == "__main__":										# Ejecuto la aplicación			
  aplicacion.run()