# Las listas son mutables = dinamicas

frutas = ['manzanas','peras','platanos']
frutas.append("fresas")
print(frutas)
frutas.pop()
print(frutas)

for i in range(0,len(frutas)):
  print("El indice ",i," esta ocupado por: ",frutas[i])

