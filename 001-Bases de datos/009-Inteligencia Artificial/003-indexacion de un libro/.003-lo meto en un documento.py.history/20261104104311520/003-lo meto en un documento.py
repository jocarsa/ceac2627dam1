archivo = open("Publicado - Aprende programación con Python.md",'r')

documento = ""
lineas = archivo.readlines()
for linea in lineas:
  documento += linea
  
archivo.close()