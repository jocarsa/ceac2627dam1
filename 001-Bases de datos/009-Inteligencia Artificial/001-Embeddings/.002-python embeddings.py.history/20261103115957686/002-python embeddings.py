import requests

ruta = "http://localhost:11434/api/generate"
modelo = "nomic-embed-text:latest"
pregunta = "gato"
flujo = False
r = requests.post(ruta, json={
    "model":modelo,
    "prompt": pregunta,
    "stream": flujo
})
print(r.json()["response"])