import os
import sys
import time
import random


from io import BytesIO

import requests
import json
import hmac, hashlib
import binascii
import base64

from PIL import Image
from adbui import ocr

im=r'C:\Users\ljy\Desktop\MyDemo\PythonDemo\my_selenium\screenshots\1610035850.4627576.png'

ocr.Ocr(app_id='10140931', secret_id='AKIDqa9WiikFqJbhbJ9cAWgfS3b9WgeTJYoy', secret_key='84oMjvvjLl02sW2NVSDl8IG1axAF8pKe')

AppID ='10140931'
SecretID='AKIDqa9WiikFqJbhbJ9cAWgfS3b9WgeTJYoy'
SecretKey='84oMjvvjLl02sW2NVSDl8IG1axAF8pKe'
user_id='401031711'
expired=int(time.time()) + 2592000

now = int(time.time())
rdm = random.randint(0, 999999999)
plain_text = 'a=' + AppID + '&k=' + SecretID + '&e=' + str(expired) + '&t=' + str(now) + '&r=' + str(rdm) + '&u=' + user_id + '&f='


#plain_text = 'u=' + user_id +'&a=' + AppID + '&k=' + SecretID + '&e=' + str(expired) + '&t=' + str(now) + '&r=' + str(rdm)   + '&f='

b = hmac.new(SecretKey.encode(), plain_text.encode(), hashlib.sha1)
s = b.hexdigest()
s = binascii.unhexlify(s)
s = s + plain_text.encode('ascii')
signature = base64.b64encode(s).rstrip()  # 生成签名
print(signature)

headers = {'Authorization': signature, 'Content-Type': 'text/json'}
url = 'http://api.youtu.qq.com/youtu/ocrapi/generalocr'
buffered = BytesIO()
image = Image.open(im)
image.save(buffered, format="png")
image = base64.b64encode(buffered.getvalue())
data = {"app_id": AppID, "session_id": '', "image": image.rstrip().decode('utf-8')}

try:
    r = requests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code != 200:
        print({'httpcode': r.status_code, 'errorcode': '', 'errormsg': ''})
    r.encoding = 'utf-8'
    result = r.json()
    print(result)
except Exception as e:
    print({'httpcode': 0, 'errorcode': 'IMAGE_NETWORK_ERROR', 'errormsg': str(e)})