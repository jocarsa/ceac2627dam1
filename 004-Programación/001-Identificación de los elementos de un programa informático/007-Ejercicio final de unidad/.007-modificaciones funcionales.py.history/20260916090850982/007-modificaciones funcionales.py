"""
	Calculadora de IVA
  Versión 0.1
  por Jose Vicente Carratala
"""

# OPERACIONES DE ENTRADA - METEMOS INFORMACIÓN EN EL PROGRAMA
print("-"*60)
print("Bienvenidos al programa calculadora") 	# Salida
print("-"*60)
base = input("Introduce la base imponible: ")	# Entrada y variable
porcentaje = input("Introduce el porcentaje de impuesto: ")

# OPERACIONES DE CÁLCULO - TRABAJAMOS CON LA INFORMACIÓN
base = int(base)										# Convierto el tipo en entero
porcentaje = int(porcentaje)				# Convierto el tipo en entero
iva = base * (porcentaje/100)										# Operadores = literales
total = base + iva									# Siguen siendo operadores

# OPERACIONES DE SALIDA - EL PROGRAMA NOS DA LOS RESULTADOS
print("-"*30)
print("Totales de la factura:")
print("Base imponible: ",base,"€")
print("IVA: ",iva,"€")
print("Total: ",total,"€")
print("-"*30)