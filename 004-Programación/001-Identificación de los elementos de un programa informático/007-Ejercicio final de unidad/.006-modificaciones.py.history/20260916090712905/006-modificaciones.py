"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("-"*30)
print("Bienvenidos al programa calculadora") 	# Salida
print("-"*30)
base = input("Introduce la base imponible: ")	# Entrada y variable

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
iva = base * 0.21										# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("-"*30)
print("Totales de la factura:")
print("Base imponible: ",base,"€")
print("IVA: ",iva,"€")
print("Total: ",total,"€")
print("-"*30)