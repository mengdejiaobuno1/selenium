import re

from PIL import Image
from adbui import ocr

AppID ='10140931'
SecretID='AKIDqa9WiikFqJbhbJ9cAWgfS3b9WgeTJYoy'
SecretKey='84oMjvvjLl02sW2NVSDl8IG1axAF8pKe'
user_id='401031711'



app_id = '10126986'
secret_id = 'AKIDT1Ws34B98MgtvmqRIC4oQr7CBzhEPvCL'
secret_key = 'AAyb3KQL5d1DE4jIMF2f6PYWJvLaeXEk'

im=r"C:\Users\ljy\Desktop\MyDemo\PythonDemo\my_selenium\screenshots\1610035850.4627576.png"

image = Image.open(im,formats=['JPEG'])
#o = ocr.Ocr(app_id=app_id, secret_id=secret_id, secret_key=secret_key)
o = ocr.Ocr(app_id=AppID, secret_id=SecretID, secret_key=SecretKey)

t = o.get_result_image(image)
print(t)
