from flask import Flask,render_template,request
import mysql.connector

connection = mysql.connector.connect(
        host='localhost',
        user='medicos',
        password='CEAC123$',
        database='medicos'
    )


aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("formulario.html")

@aplicacion.route("/recogedatos",methods=['POST'])
def recogedatos():
  cursor = connection.cursor()
  cursor.execute("""
        INSERT INTO medicos (nombre, especialidad, numero_de_colegiado)
        VALUES (%s, %s, %s);
    """, (
        request.form["nombre"],
        request.form["especialidad"],
        request.form["numero_de_colegiado"]
    ))
  connection.commit()
  return render_template("confirmacion.html")

if __name__ == "__main__":
  aplicacion.run()

cursor.close()
conexion.close()
