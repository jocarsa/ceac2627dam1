import requests

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"
pregunta = "gato"

r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})

embeddings = r.json()["embeddings"][0]
print(embeddings[0])