import requests
archivo = open("Publicado - Aprende programación con Python.md",'r')

cacho = 40
solapado = 5
documento = ""
lineas = archivo.readlines()
for linea in lineas:
  documento += linea
  
for i in range(0,len(documento),cacho):
  print(documento[i:i+cacho+solapado])
  
archivo.close()