import requests

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"
# GATO ############################################
pregunta = "gato"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
gato = r.json()["embeddings"][0]
# PERRO ############################################
pregunta = "perro"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
perro = r.json()["embeddings"][0]