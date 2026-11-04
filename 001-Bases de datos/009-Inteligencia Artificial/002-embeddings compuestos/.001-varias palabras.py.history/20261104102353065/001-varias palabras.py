import requests

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"
# GATO ############################################
pregunta = "estoy viviendo en Valencia"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
gato = r.json()["embeddings"][0]

perro = r.json()["embeddings"][0]