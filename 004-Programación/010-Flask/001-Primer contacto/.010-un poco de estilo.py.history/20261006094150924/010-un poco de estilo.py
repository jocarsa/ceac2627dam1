# En primer lugar importo la librería
from flask import Flask

# Ahora creo una aplicación base
aplicacion = Flask("__name__") 

# Defino un punto donde flask va a escuchar en la web
@aplicacion.route("/")
def inicio():
  cadena = "<style>div{width:50px;height:50px;border:1px solid grey;float:left;}</style>"
  # Recordamos cómo hacer estructuras de bucle
  for dia in range(1,31):
    cadena += "<div>"+str(dia)+"</duv>"
  return cadena

# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run()