def encriptar(entrada):
  salida = ""
  for letra in entrada:
  	salida += chr(ord(letra)+5)
  return salida

def desencriptar(entrada):
  salida = ""
  for letra in entrada:
  	salida += chr(ord(letra)-5)
  return salida

print(encriptar("Jose Vicente"))
print(encriptar("Esto es una frase de prueba que estoy encriptando"))
