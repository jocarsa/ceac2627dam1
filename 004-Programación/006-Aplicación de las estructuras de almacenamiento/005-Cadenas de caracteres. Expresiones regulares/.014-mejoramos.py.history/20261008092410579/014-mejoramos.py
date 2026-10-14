mail = "info@jocarsa.com"
noemail = "hola@adios"

contador = 0
for letra in mail:
  if letra == "@" or letra == ".":
    esmail = True
print(esmail)

esmail = False
for letra in noemail:
  if letra == "@":
    esmail = True
print(esmail)