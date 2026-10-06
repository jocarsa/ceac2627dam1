from flask import Flask

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return "Si estas viendo esto te lo está dando Python"

if __name__ == "__main__":
  aplicacion.run()