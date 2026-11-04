import requests

r = requests.post("http://localhost:11434/api/generate", json={
    "model": "qwen3.5:0.8b",
    "prompt": "Hola quien eres",
    "stream": False
})

print(r.json()["response"])