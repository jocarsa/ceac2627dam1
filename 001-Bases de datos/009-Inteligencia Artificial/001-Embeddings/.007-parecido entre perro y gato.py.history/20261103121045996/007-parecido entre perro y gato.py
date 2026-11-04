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

for i in range(0,len(miercoles)):
  print("gato:",gato[i]," - miercoles dice:",miercoles[i]," - diferencia=",abs(gato[i]-miercoles[i]))