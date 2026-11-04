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
    "gatito"
]

r = requests.post(ruta, json={
    "model": modelo,
    "input": palabras
})
r.raise_for_status()

vectores = r.json()["embeddings"]

def coseno(a, b):
    producto = sum(x*y for x, y in zip(a, b))
    norma_a = math.sqrt(sum(x*x for x in a))
    norma_b = math.sqrt(sum(y*y for y in b))
    return producto / (norma_a * norma_b)

# Cabecera de la tabla
print(f"{'':15}", end="")

for palabra in palabras:
    print(f"{palabra:12}", end="")

print()

# Matriz de similitudes
for i, palabra in enumerate(palabras):

    print(f"{palabra:15}", end="")

    for j in range(len(palabras)):
        puntuacion = coseno(vectores[i], vectores[j])
        print(f"{puntuacion:12.4f}", end="")

    print()