import pytesseract
from PIL import Image

png = 'C:\\Users\\ljy\\Desktop\\MyDemo\\PythonDemo\\my_selenium\\screenshots\\1.png'

#print(pytesseract.image_to_string(png))


print(pytesseract.image_to_string(Image.open(png)))