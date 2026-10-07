"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

print("Bienvenidos al programa calculadora") 	# Salida
base = input("Introduce la base imponible: ")	# Entrada y variable

base = int(base)										# Convierto el tipo en entero
iva = base * 0.21										# Operadores = literales
total = base + iva									# Siguen siendo operadores

print("Totales de la factura:")
print("Base imponible: ",base)
print("IVA: ",iva)
print("Total: ",total)