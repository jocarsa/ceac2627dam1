import requests

# Defino la ruta donde ollama está escuchando (esto es fijo)
ruta = "http://localhost:11434/api/generate"
# Elijo un modelo de entre los que he descargado
modelo = "qwen3.5:0.8b"
pregunta = "Hola quien eres?"
flujo = False
r = requests.post(ruta, json={
    "model": ,modelo
    "prompt": pregunta,
    "stream": flujo
})

print(r.json()["response"])