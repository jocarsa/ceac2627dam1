from flask import Flask, render_template
import requests

aplicacion = Flask("__name__") 

@aplicacion.route("/")
def inicio():
  return render_template("index.html")
  
if __name__ == "__main__":
  aplicacion.run()