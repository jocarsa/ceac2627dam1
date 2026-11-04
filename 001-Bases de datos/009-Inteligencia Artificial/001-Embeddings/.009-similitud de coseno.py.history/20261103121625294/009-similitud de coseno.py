import requests
import math

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"

def embedding(texto):
    r = requests.post(ruta, json={
        "model": modelo,
        "input": texto
    })
    r.raise_for_status()
    return r.json()["embeddings"][0]

def similitud(a, b):
    producto = sum(x*y for x,y in zip(a,b))
    norma_a = math.sqrt(sum(x*x for x in a))
    norma_b = math.sqrt(sum(y*y for y in b))

    return producto / (norma_a * norma_b)

gato = embedding("gato")
miercoles = embedding("miércoles")

print(similitud(gato, miercoles))