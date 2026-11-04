import requests

ruta = "http://localhost:11434/api/generate"
modelo = "qwen3.5:0.8b"
pregunta = "Hola quien eres?"
r = requests.post(ruta, json={
    "model": ,modelo
    "prompt": ,
    "stream": False
})

print(r.json()["response"])