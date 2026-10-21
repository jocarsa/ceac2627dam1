from flask import Flask,render_template,request

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos",methods=['POST'])
def sobremi():
  cadena =""
  cadena += "Nombre del médico: "+request.form['nombre']+"<br>"
  cadena += "Especialidad del médico: "+request.form['especialidad']+"<br>"
  cadena += "Número de colegiado del médico: "+request.form['numero_de_colegiado']+"<br>"
  return "yo voy a recoger tus datos"



if __name__ == "__main__":
  aplicacion.run()