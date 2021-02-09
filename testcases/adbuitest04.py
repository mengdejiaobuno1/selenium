# coding=utf-8
# /usr/bin/python
# coding=utf-8
# create by 15025463191 2017/10/11

import requests
import hmac
import hashlib
import base64
import time
import random
import re

appid = "10140931"
bucket = "imgregnise"
secret_id = "AKIDqa9WiikFqJbhbJ9cAWgfS3b9WgeTJYoy"  #我更改了，不要复制我的
secret_key = b"84oMjvvjLl02sW2NVSDl8IG1axAF8pKe"  #我更改了，不要复制我的
expired = time.time() + 2592000
onceExpired = 0
current = time.time()
rdm = ''.join(random.choice("0123456789") for i in range(10))
userid = "0"
fileid = "tencentyunSignTest"

info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(
    rdm) + "&u=0&f="

signindex = hmac.new(secret_key, info.encode(), hashlib.sha1).digest()  # HMAC-SHA1加密
sign = base64.b64encode(signindex + info.encode())  # base64转码

url = "http://recognition.image.myqcloud.com/ocr/general"
headers = {'Host': 'recognition.image.myqcloud.com',
           "Content-Length": "187",
           "Content-Type": "application/json",
           "Authorization": sign
           }

payload = {
    "appid": appid,
    "bucket": bucket,
    "url": "http://imgregnise-1254602529.picsh.myqcloud.com/123456.png"
}

r = requests.post(url, json=payload, headers=headers)
responseinfo = r.content

r_index = r'itemstring":"(.*?)"'  # 做一个正则匹配
result = re.findall(r_index, responseinfo)
for i in result:
    print(i)