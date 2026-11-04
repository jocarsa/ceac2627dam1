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
# miercoles ############################################
pregunta = "miercoles"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
miercoles = r.json()["embeddings"][0]

diferencia = 0
for i in range(0,len(miercoles)):
  diferencia += abs(miercoles[i]-gato[i])
  
print(diferencia)
  