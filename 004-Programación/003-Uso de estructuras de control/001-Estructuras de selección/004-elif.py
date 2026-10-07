edad = input("Dime tu edad: ")
edad = int(edad)
if edad < 10:
	print("Eres un niño")
elif edad >=10 and edad < 20:
  print("Eres un adolescente")
elif edad >=20 and edad < 30:
  print("Eres un joven")
elif edad >=30 and edad < 40:
  print("Eres un adulto")
else:
  print("Eres un viejo")