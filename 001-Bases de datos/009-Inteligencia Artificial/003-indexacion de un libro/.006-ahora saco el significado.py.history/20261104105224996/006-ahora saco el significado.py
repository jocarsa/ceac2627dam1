import requests
archivo = open("Publicado - Aprende programación con Python.md",'r')


ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"

cacho = 40
solapado = 5
documento = ""
lineas = archivo.readlines()
for linea in lineas:
  documento += linea
  
for i in range(0,len(documento),cacho):
  cacho = documento[i:i+cacho+solapado]
  r = requests.post(ruta, json={
      "model": modelo,
      "input": cacho
  })
  respuesta = r.json()["embeddings"][0]
  print(cacho)
  print(respusta)
  print("-"*50)
  
archivo.close()