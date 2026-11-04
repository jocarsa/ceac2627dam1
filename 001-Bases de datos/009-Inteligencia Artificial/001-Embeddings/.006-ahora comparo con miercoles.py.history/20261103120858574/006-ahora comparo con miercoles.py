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
pregunta = "miercoles"
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
miercoles = r.json()["embeddings"][0]

for i in range(0,len(perro)):
  print("gato:",gato[i]," - perro dice:",perro[i]," - diferencia=",abs(gato[i]-perro[i]))