import requests
import math

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"

palabras = [
  "ordenador",
    "gato",
    "perro",
    "felino",
    "automóvil",
    "miércoles",
    "mascota",
    "gatito",
    
]

r = requests.post(ruta, json={
    "model": modelo,
    "input": palabras
})
r.raise_for_status()

vectores = r.json()["embeddings"]

def coseno(a, b):
    producto = sum(x*y for x,y in zip(a,b))
    norma_a = math.sqrt(sum(x*x for x in a))
    norma_b = math.sqrt(sum(y*y for y in b))
    return producto / (norma_a * norma_b)

referencia = vectores[0]

resultados = []

for palabra, vector in zip(palabras, vectores):
    puntuacion = coseno(referencia, vector)
    resultados.append((palabra, puntuacion))

resultados.sort(key=lambda x: x[1], reverse=True)

for palabra, puntuacion in resultados:
    print(f"{palabra:15} {puntuacion:.4f}")