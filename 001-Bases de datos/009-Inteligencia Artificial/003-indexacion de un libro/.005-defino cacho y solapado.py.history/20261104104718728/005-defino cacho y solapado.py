archivo = open("Publicado - Aprende programación con Python.md",'r')

cacho = 20
solapado = 5
documento = ""
lineas = archivo.readlines()
for linea in lineas:
  documento += linea
  
for i in range(0,len(documento),cacho):
  print(documento[i,cacho+solapado])
  
archivo.close()