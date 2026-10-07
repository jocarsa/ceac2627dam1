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
        	width:100%;height:50px;border-left:1px solid grey;
          border-top:1px solid grey;float:left;
          padding:5px;font-family:sans-serif;
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