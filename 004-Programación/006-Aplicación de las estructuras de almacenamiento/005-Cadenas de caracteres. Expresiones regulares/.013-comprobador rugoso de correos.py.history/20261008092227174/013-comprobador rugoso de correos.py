mail = "info@jocarsa.com"
noemail = "Hola como estas"

esmail = False
for letra in mail:
  if letra == "@":
    esmail = True
print(esmail)

esmail = False
for letra in noemail:
  if letra == "@":
    esmail = True
print(esmail)