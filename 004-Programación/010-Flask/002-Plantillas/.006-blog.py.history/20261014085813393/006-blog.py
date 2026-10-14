from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"blog.html",
    	titulo = "El blog de Jose Vicente",
    	subtitulo = "Esto es un blog"
    	articulos = [
      	{"titulo":"Articulo 1","contenido":"Este es el contenido del articulo 1"}
      ]
  )
  
if __name__ == "__main__":
  aplicacion.run()