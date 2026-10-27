# Importo la librería de bases de datos
import sqlite3

# Importo la librería de web
from flask import Flask, render_template, request

# Creo una aplicación web
aplicacion = Flask(__name__)

# Escucho en la raíz /
@aplicacion.route("/")
def inicio():
    # Me conecto a la base de datos
    conexion = sqlite3.connect("blog.db")

    # Lo que venga lo quiero como diccionario
    conexion.row_factory = sqlite3.Row

    # Creo un cursor necesario
    cursor = conexion.cursor()

    # Le pido los artículos
    cursor.execute("SELECT * FROM articulos")

    # Cargo los artículos en una variable
    articulos = cursor.fetchall()

    # Cierro la conexión
    conexion.close()

    # Pinto la plantilla
    return render_template("frente.html", datos=articulos)


if __name__ == "__main__":
    aplicacion.run()