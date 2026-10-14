import re

email = "info@jocarsa.com"
noemail = "****hola%%%.***quetal.com"

patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

print(re.fullmatch(patron, email))    # True
print(re.fullmatch(patron, noemail))  # False