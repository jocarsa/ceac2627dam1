from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"index3.html",
    nombre = "Jose Vicente",
    apellidos = "Carratala Sanchis",
    email = "info@jocarsa.com"
  )
  
if __name__ == "__main__":
  aplicacion.run()