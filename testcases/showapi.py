from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "511292", "1ae614420cea41e997ac700460b929f6")
r.addFilePara("image", r"C:\Users\ljy\Desktop\MyDemo\PythonDemo\my_selenium\screenshots\1610035850.4627576.png")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
print(res.text)  # 返回信息
