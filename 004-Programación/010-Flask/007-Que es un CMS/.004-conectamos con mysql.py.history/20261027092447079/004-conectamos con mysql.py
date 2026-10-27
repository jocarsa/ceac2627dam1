# Flask permite crear webs
# render_template permite llamar a html
# request permite enviar información en formularios
from flask import Flask,render_template,request
# Importamos el conector de MySQL
import mysql.connector

# Me conecto a la base de datos que hemos creado
connection = mysql.connector.connect(
        host='localhost',
        user='blogceacdam2627',
        password='CEAC123$',
        database='blogceacdam2627'
    )
# en MySQL hay que crear un cursor (transporta los datos)
cursor = connection.cursor(dictionary=True)
# Creo una aplicación web
aplicacion = Flask("__name__") 

# Defino la ruta de inicio
@aplicacion.route("/")
def inicio():
  # Dame  todos los articulos de la base de datos
  cursor.execute("SELECT * FROM articulos")
  # Los meto en una variable
  articulos = cursor.fetchall()
  # Llamo a la plantilla Y LE PASO LOS ARTICULOS
  return render_template("frente.html",articulos=articulos)

@aplicacion.route("/tabla")
def tabla():
  # Dame  todos los articulos de la base de datos
  cursor.execute("SELECT * FROM articulos")
  # Los meto en una variable
  articulos = cursor.fetchall()
  # Llamo a la plantilla Y LE PASO LOS ARTICULOS
  return render_template("tabla.html",articulos=articulos)

@aplicacion.route("/formulario")
def formulario():
  return render_template("formulario.html")

@aplicacion.route("/inserta",methods=['POST'])
def inserta():
  return render_template("inserta.html")

if __name__ == "__main__":
  aplicacion.run()