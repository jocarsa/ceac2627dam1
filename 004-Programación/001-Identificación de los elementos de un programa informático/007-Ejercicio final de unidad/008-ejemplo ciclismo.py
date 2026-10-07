"""
	Calculadora de Pedaladas
  Versión 0.1
  por Jose Vicente Carratala
"""

# Estas son las condiciones iniciales
PEDALADA = 1.5

# Entrada del usuario	
numero_pedaladas = input("Cuantas pedaladas has dado?: ")
numero_pedaladas = int(numero_pedaladas)

# ahora hacemos cálculos
avance = numero_pedaladas*PEDALADA

# Operaciones de salida
print("Has dado",numero_pedaladas,"pedaladas")
print("Cada pedalada son ",pedalada,"metros")
print("Pues has avanzado",avance,"metros")