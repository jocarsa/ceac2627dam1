import requests

# Defino la ruta donde ollama está escuchando (esto es fijo)
ruta = "http://localhost:11434/api/generate"
# Elijo un modelo de entre los que he descargado
modelo = "qwen3.5:0.8b"
# Establezco una pregunta
pregunta = "Hola quien eres?"
# Elijo si me suelta la respuesta de golpe o palabra a palabra
flujo = False
r = requests.post(ruta, json={
    "model": ,modelo
    "prompt": pregunta,
    "stream": flujo
})

print(r.json()["response"])