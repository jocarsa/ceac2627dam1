
import pytesseract
from PIL import Image

imagen = Image.open("dni.jpg")

texto = pytesseract.image_to_string(imagen, lang="spa")

print(texto)
