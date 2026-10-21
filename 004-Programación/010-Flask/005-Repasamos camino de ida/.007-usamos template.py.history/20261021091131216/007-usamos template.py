from flask import Flask,render_template,request

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos",methods=['POST'])
def sobremi():
  return render_template("confirmacion.html")



if __name__ == "__main__":
  aplicacion.run()