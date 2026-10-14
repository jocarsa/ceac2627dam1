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

cadena = "Jose Vicente"
encriptado = encriptar(cadena)
desencriptado = desencriptar(encriptado)

print(cadena)
