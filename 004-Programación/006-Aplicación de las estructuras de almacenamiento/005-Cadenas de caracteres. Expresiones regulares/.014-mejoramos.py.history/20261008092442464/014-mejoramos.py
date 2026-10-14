mail = "info@jocarsa.com"
noemail = "hola@adios"

contador = 0
for letra in mail:
  if letra == "@" or letra == ".":
    contador += 1
if contador == 2:
  print("es un correo")
else:
  print("no es un correo")

esmail = False
for letra in noemail:
  if letra == "@":
    esmail = True
print(esmail)