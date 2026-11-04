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
  cachodocumento = documento[i:i+cacho+solapado]
  r = requests.post(ruta, json={
      "model": modelo,
      "input": cachodocumento
  })
  respuesta = r.json()["embeddings"][0]
  print(cacho)
  print(respuesta)
  print("-"*50)
  
archivo.close()