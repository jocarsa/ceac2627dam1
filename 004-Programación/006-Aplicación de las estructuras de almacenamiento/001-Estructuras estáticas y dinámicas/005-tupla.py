compra = ("manzanas", "fresas")

# compra.append("platanos")

# compra.pop("platanos")

compra = list(compra)
compra[0] = "platanos"
compra = tuple(compra)

print(compra)