
import pytesseract
from PIL import Image

imagen = Image.open("documento.jpg")

texto = pytesseract.image_to_string(imagen, lang="eng")

print(texto)
