# Importo la librería de bases de datos
import sqlite3
# Importo la librería de web
from flask import Flask,render_template,request

# Me conecto a la base de datos
conexion = sqlite3.connect("blog.db")
# Lo que venga lo quiero como diccioario
conexion.row_factory = sqlite3.Row

# creo una aplicacion web
aplicacion = Flask("__name__") 

# escucho en la raiz /
@aplicacion.route("/")
def inicio():
  # Creo un cursor necesario
	cursor = conexion.cursor()
  # Le pido los articulos
	cursor.execute("SELECT * FROM articulos")
	articulos = cursor.fetchall()
	return render_template("frente.html",datos=articulos)


if __name__ == "__main__":
  aplicacion.run()
  
conexion.close()