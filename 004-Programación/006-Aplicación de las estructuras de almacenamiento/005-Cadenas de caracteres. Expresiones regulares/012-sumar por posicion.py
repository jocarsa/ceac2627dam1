
def encriptar(entrada):
    salida = ""
    contador = 0
    for letra in entrada:
        salida += chr(ord(letra) + contador)
        contador += 1
    return salida

def desencriptar(entrada):
    salida = ""
    contador = 0
    for letra in entrada:
        salida += chr(ord(letra) - contador)
        contador += 1
    return salida

cadena = "Jose Vicente"
encriptado = encriptar(cadena)
desencriptado = desencriptar(encriptado)

print(cadena)
print(encriptado)
print(desencriptado)
