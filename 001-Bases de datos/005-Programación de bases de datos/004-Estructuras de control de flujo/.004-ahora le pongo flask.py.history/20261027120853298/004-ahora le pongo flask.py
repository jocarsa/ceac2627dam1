# Importo la librería de bases de datos
import sqlite3
# Importo la librería de web
from flask import Flask,render_template,request

conexion = sqlite3.connect("blog.db")
conexion.row_factory = sqlite3.Row

aplicacion = Flask("__name__") 


@aplicacion.route("/")
def inicio():
  return render_template("frente.html")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM articulos")

for fila in cursor.fetchall():
    print(dict(fila))



if __name__ == "__main__":
  aplicacion.run()
  
conexion.close()