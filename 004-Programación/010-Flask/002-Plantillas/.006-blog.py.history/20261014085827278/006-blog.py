from flask import Flask, render_template

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template(
    	"blog.html",
    	titulo = "El blog de Jose Vicente",
    	subtitulo = "Esto es un blog"
    	articulos = [
      	{"titulo":"Articulo 1","contenido":"Este es el contenido del articulo 1"},
        {"titulo":"Articulo 2","contenido":"Este es el contenido del articulo 2"},
        {"titulo":"Articulo 3","contenido":"Este es el contenido del articulo 3"},
        {"titulo":"Articulo 4","contenido":"Este es el contenido del articulo 4"},
      ]
  )
  
if __name__ == "__main__":
  aplicacion.run()