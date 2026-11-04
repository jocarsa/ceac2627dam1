from flask import Flask,render_template				# En primer lugar importo la librería

aplicacion = Flask("__name__") 								# Ahora creo una aplicación base

@aplicacion.route("/")												# Defino un punto donde flask va a escuchar en la web
def inicio():
  return render_template("principal.html")

if __name__ == "__main__":										# Ejecuto la aplicación			
  aplicacion.run()