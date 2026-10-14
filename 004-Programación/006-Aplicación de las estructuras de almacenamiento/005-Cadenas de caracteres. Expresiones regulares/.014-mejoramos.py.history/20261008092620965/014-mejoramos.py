mail = "info@jocarsa.com"
noemail = "***caca*&%@adios***.com"

contador = 0
for letra in mail:
  if letra == "@" or letra == ".":
    contador += 1
if contador == 2:
  print("es un correo")
else:
  print("no es un correo")

contador = 0
for letra in noemail:
  if letra == "@" or letra == ".":
    contador += 1
if contador == 2:
  print("es un correo")
else:
  print("no es un correo")