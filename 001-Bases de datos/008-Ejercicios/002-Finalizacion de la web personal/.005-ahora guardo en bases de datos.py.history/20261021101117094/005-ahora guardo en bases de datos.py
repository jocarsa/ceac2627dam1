from flask import Flask,render_template,request
import mysql.connector

aplicacion = Flask("__name__") 

connection = mysql.connector.connect(
  host='localhost',
  user='miweb',
  password='CEAC123$',
  database='miweb'
)

cursor = connection.cursor(dictionary = True)

@aplicacion.route("/")
def inicio():
  return render_template("inicio.html")

@aplicacion.route("/sobremi")
def sobremi():
  return render_template("sobremi.html")

@aplicacion.route("/proyectos")
def proyectos():
  print("Hola")
  cursor.execute("SELECT * FROM proyectos") # Saco los proyectos de la base de datos
  proyectos = cursor.fetchall()		# Los meto en una variable
  print(proyectos)
  return render_template("proyectos.html",proyectos=proyectos) # Y se los paso a la plantilla

@aplicacion.route("/contacto")
def contacto():
  return render_template("contacto.html")

@aplicacion.route("/recibedatos",methods=['POST'])
def recibedatos():
  cursor.execute("""
  	INSERT INTO contacto VALUES(
    	NULL,
      '"""+request.form['nombre']+"""',
      '"""+request.form['correo']+"""',
      '"""+request.form['correo']+"""'
    );
    """)
  conexion.commit()
  return render_template("confirmacion.html")

if __name__ == "__main__":
  aplicacion.run()
  
cursor.close()
connection.close()