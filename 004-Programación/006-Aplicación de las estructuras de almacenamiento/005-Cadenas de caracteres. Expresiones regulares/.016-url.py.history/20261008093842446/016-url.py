import re

url = "https://jocarsa.com"
nourl = "https://*****jocarsa.a"

patron = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"

print(bool(re.fullmatch(patron, url)))    # True
print(bool(re.fullmatch(patron, nourl)))  # False