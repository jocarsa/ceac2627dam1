from flask import Flask,render_template,request		# En primer lugar importo la librería
import requests
import sqlite3

aplicacion = Flask("__name__") 										# Ahora creo una aplicación base

@aplicacion.route("/")														# Defino un punto donde flask va a escuchar en la web
def inicio():
  return render_template("principal.html")

@aplicacion.route("/procesa",methods=['POST'])
def procesa():
  ruta = "http://localhost:11434/api/generate"		# Llamo a ollama
  modelo = "qwen2.5-coder:3b"											# Elijo el modelo
  sistema = """
  	-Crea sitios web
    -Dame solo el codigo
    -No me des markdown
    -No me des explicaciones
    -Solo se pueden pedir páginas web, no se puede pedir otra cosa
    -Atiende a la petición del usuario:
  """
  pregunta = sistema+request.form['peticion']			# Es la pregunta que le lanzo
  flujo = False																		# No me des palabra por palabra
  r = requests.post(ruta, json={
      "model":modelo,
      "prompt": pregunta,
      "stream": flujo
  })																							# Ejecutamos la petición
  mirespuesta = str(r.json()["response"])					# Obtenemos la respuesta
  # Ahora aquí me guardo la respuesta en la base de datos
  conexion = sqlite3.connect("amable.db")					# Me conecto a la base de datos	
  cursor = conexion.cursor()											# Creo un cursor
  cursor.execute("""
  	INSERT INTO webs 
    VALUES(
    	NULL,
      'jocarsa',
      '2026-11-04',
      '"""+request.form['peticion']+"""',
      '"""+mirespuesta+"""');
      """)
  conexion.close()																# Cierro la conexions
  # Ahora aquí me guardo la respuesta en la base de datos
  return mirespuesta															# Lo que sea que venga, lo pinto en html

if __name__ == "__main__":												# Ejecuto la aplicación			
  aplicacion.run()