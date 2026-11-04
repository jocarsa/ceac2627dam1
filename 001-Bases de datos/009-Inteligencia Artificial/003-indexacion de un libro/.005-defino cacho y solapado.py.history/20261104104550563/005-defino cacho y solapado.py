archivo = open("Publicado - Aprende programación con Python.md",'r')

cacho = 20
solapado = 5
documento = ""
lineas = archivo.readlines()
for linea in lineas:
  documento += linea
  
print(documento[0])
  
archivo.close()