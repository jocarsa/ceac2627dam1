import requests

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"
pregunta = "gato"

r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})

print(r.json()["embeddings"][0])