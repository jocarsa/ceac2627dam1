import json
nombre = input("Dime como te llamas: ")
apellidos = input("Dime tus apellidos: ")
email = input("Dime tu email: ")
telefono = input("Dime tu telefono: ")

diccionario = {
	"nombre":nombre,
  "apellidos":apellidos,
  "email":email,
  "telefono":telefono
}

archivo = open("misdatos.json", 'w')
json.dump(diccionario, archivo, indent=4, ensure_ascii=False)
archivo.close()