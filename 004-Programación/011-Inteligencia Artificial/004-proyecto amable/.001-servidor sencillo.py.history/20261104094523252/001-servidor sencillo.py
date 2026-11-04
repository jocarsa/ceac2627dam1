
from flask import Flask							# En primer lugar importo la librería


aplicacion = Flask("__name__") 			# Ahora creo una aplicación base


@aplicacion.route("/")							# Defino un punto donde flask va a escuchar en la web
def inicio():
  return "Si estas viendo esto te lo está dando Python"
# Ejecuto la aplicación
if __name__ == "__main__":					

  aplicacion.run()