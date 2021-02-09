# coding=utf-8
from adbui import Device
import sys,os,time

d=Device()
d.init_ocr('10140931', 'AKIDqa9WiikFqJbhbJ9cAWgfS3b9WgeTJYoy', '84oMjvvjLl02sW2NVSDl8IG1axAF8pKe')


btn2 = d.get_ui_by_ocr(text='8396')
btn2.click()
d.adb_ext.input('18656108396')

time.sleep(2)

btn3 = d.get_ui_by_ocr(text='输入登录密码')
btn3.click()
d.adb_ext.input('4651079li')

time.sleep(2)
btn4 = d.get_uis_by_ocr(text='登录', is_update=True)
time.sleep(2)
print(btn4)
btn4[3].click()
time.sleep(2)
btn5 = d.get_uis_by_ocr(text='登录',is_update=True)
btn5[3].click()