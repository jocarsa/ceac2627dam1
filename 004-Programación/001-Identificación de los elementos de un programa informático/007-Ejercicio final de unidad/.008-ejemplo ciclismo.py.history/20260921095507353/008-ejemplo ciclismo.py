# Estas son las condiciones iniciales
pedalada = 1.5

# Entrada del usuario	
numero_pedaladas = input("Cuantas pedaladas has dado?: ")
numero_pedaladas = int(numero_pedaladas)

# ahora hacemos cálculos
avance = numero_pedaladas*pedalada

# Operaciones de salida
print("Has dado",numero_pedaladas,"pedaladas")
print("Pues has avanzado",avance,"metros")