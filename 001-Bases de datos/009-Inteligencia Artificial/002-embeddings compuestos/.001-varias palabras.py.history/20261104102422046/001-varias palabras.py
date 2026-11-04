import requests

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"
# GATO ############################################
pregunta = "estoy viviendo en Valencia"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
respuesta = r.json()["embeddings"][0]

print(respuesta)
