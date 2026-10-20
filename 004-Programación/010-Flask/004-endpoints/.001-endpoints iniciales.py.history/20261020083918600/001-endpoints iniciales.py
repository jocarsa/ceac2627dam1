from flask import Flask

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return "yo soy la pagina de inicio"

if __name__ == "__main__":
  aplicacion.run()