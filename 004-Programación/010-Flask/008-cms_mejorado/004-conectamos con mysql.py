import os
from datetime import date
from flask import Flask, render_template, request, redirect, url_for, flash, abort
import mysql.connector

aplicacion = Flask(__name__)
aplicacion.secret_key = os.environ.get('FLASK_SECRET_KEY', 'cambiar-en-produccion')

def conectar():
    return mysql.connector.connect(host=os.getenv('DB_HOST','localhost'), user=os.getenv('DB_USER','blogceacdam2627'), password=os.getenv('DB_PASSWORD','CEAC123$'), database=os.getenv('DB_NAME','blogceacdam2627'))

def consultar(sql, parametros=(), uno=False):
    conexion = conectar()
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(sql, parametros)
        resultado = cursor.fetchone() if uno else cursor.fetchall()
        cursor.close()
        return resultado
    finally:
        conexion.close()

def ejecutar(sql, parametros=()):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(sql, parametros)
        conexion.commit()
        cursor.close()
    finally:
        conexion.close()

@aplicacion.route('/')
def inicio():
    articulos = consultar('SELECT * FROM articulos ORDER BY fecha DESC, id DESC')
    return render_template('frente.html', articulos=articulos)

@aplicacion.route('/tabla')
def tabla():
    articulos = consultar('SELECT * FROM articulos ORDER BY fecha DESC, id DESC')
    return render_template('tabla.html', articulos=articulos)

@aplicacion.route('/formulario')
def formulario():
    return render_template('formulario.html', articulo=None, hoy=date.today().isoformat())

@aplicacion.route('/inserta', methods=['POST'])
def inserta():
    titulo = request.form.get('titulo','').strip()
    fecha = request.form.get('fecha','').strip()
    contenido = request.form.get('contenido','').strip()
    if not titulo or not fecha or not contenido:
        flash('Completa todos los campos.', 'error')
        return redirect(url_for('formulario'))
    ejecutar('INSERT INTO articulos (titulo, fecha, contenido) VALUES (%s,%s,%s)', (titulo, fecha, contenido))
    flash('Artículo publicado correctamente.', 'ok')
    return redirect(url_for('tabla'))

@aplicacion.route('/editar/<int:id>', methods=['GET','POST'])
def editar(id):
    articulo = consultar('SELECT * FROM articulos WHERE id=%s', (id,), uno=True)
    if articulo is None:
        abort(404)
    if request.method == 'POST':
        titulo = request.form.get('titulo','').strip()
        fecha = request.form.get('fecha','').strip()
        contenido = request.form.get('contenido','').strip()
        if not titulo or not fecha or not contenido:
            flash('Completa todos los campos.', 'error')
        else:
            ejecutar('UPDATE articulos SET titulo=%s, fecha=%s, contenido=%s WHERE id=%s', (titulo,fecha,contenido,id))
            flash('Artículo actualizado.', 'ok')
            return redirect(url_for('tabla'))
    return render_template('formulario.html', articulo=articulo, hoy=date.today().isoformat())

@aplicacion.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    ejecutar('DELETE FROM articulos WHERE id=%s', (id,))
    flash('Artículo eliminado.', 'ok')
    return redirect(url_for('tabla'))

if __name__ == '__main__':
    aplicacion.run(debug=True)
