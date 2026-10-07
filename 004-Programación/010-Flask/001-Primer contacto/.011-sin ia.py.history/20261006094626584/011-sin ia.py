# En primer lugar importo la librería
from flask import Flask

# Ahora creo una aplicación base
aplicacion = Flask("__name__") 

# Defino un punto donde flask va a escuchar en la web
@aplicacion.route("/")
def inicio():
  cadena = """
  <!doctype html>
  <html>
  	<head>
    	<style>
      	main{
        	display:grid;
          grid-template-columns:repeat(7,1fr);
          }
      	div{
        	width:50px;height:50px;border:1px solid grey;float:left;
          }
      </style>
    </head>
    <body>
    <main>
  """
  # Recordamos cómo hacer estructuras de bucle
  for dia in range(1,31):
    cadena += "<div>"+str(dia)+"</div>"
  cadena += """
  		</main>
  	</body>
  </html>
  """
  return cadena

# Ejecuto la aplicación
if __name__ == "__main__":
  aplicacion.run()