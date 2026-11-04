# En primer lugar importo la librería
from flask import Flask

# Ahora creo una aplicación base
aplicacion = Flask("__name__") 

# Defino un punto donde flask va a escuchar en la web
@aplicacion.route("/")
def inicio():
  return "Si estas viendo esto te lo está dando Python"

# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run()