tupla = ("manzanas","platanos")

# Puedo convertir una tupla en una lista

print(tupla)
lista = list(tupla)
print(lista)
# Ahora puedo hacer lo que quiera
lista.append("fresas")
print(lista)
# Ahora vuelvo a convertir a tupla
tupla = tuple(lista)
print(tupla)