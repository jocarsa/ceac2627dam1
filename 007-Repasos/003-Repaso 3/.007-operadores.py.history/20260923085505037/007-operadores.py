# Presentacion
TITULO = "Calculadora de distancia recorrida v"
VERSION = 0.1
print(TITULO+str(VERSION))
# Condiciones globales
tiempo_en_carretera = 0
velocidad = 0
# El usuario introduce datos
tiempo_en_carretera = input("Introduce el tiempo que llevas conduciendo: ")
velocidad = input("Introduce la velocidad a la que vas: ")

tiempo_en_carretera = float(tiempo_en_carretera)
velocidad = int(velocidad)

# El programa hace calculos
distancia = tiempo_en_carretera*velocidad

# El programa ofrece resultados
print("Has estado en carretera "+str(tiempo_en_carretera)+" h")
print("Has circulado a "+str(velocidad)+" Km/h")
print("Por lo tanto has recorrido "+str(distancia)+" Km")
