from flask import Flask,render_template,request	# Importo flask para crear una web
import json	# Importo json para poder enviar json
import sqlite3	# Import sqlite3 para poder conectarme a una base de datos

aplicacion = Flask("__name__") 

# ruta de la tienda
@aplicacion.route("/")
def inicio():
  return render_template("tienda.html")

# ruta de dame los datos
@aplicacion.route("/datos")
def datos():
    conexion = sqlite3.connect("tienda.db") # Me conecto a la base de datos
    conexion.row_factory = sqlite3.Row # Lo que venga lo quiero como diccionario
    cursor = conexion.cursor() # Creo un cursor necesario
    cursor.execute("SELECT * FROM productos") # Le pido los artículos
    productos = cursor.fetchall() # Cargo los artículos en una variable
    conexion.close() # Cierro la conexión
    return json.dumps([dict(producto) for producto in productos]) # Convierte cada fila de la base de datos en un diccionario
  
# ruta de inserta pedido
@aplicacion.route("/insertapedido",methods=['POST'])
def insertapedido():
  pedido = request.get_json()
  print(pedido)
  return "ok tu pedido ha sido insertado"

if __name__ == "__main__":
  aplicacion.run()