import pytesseract
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, time
from PIL import Image


class TestCase():
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://localhost:8080/jpress/user/register')
        self.dr.maximize_window()
        sleep(5)


    def test01(self):
        t = time()
        png = str(t) + '.png'
        fo = 'C:\\Users\\ljy\\Desktop\\MyDemo\\PythonDemo\\my_selenium\\screenshots\\' + png
        self.dr.save_screenshot(fo)
        ele = self.dr.find_element_by_xpath('//*[@id="captchaimg"]')
        sleep(3)

        dpr = self.dr.execute_script('return window.devicePixelRatio')
        left = ele.location['x']
        top = ele.location['y']
        right = left + ele.size['width']
        height = top + ele.size['height']
        print(left,top,right,height)

        t = time()
        png2 = str(t) + '.png'
        fo2 = 'C:\\Users\\ljy\\Desktop\\MyDemo\\PythonDemo\\my_selenium\\screenshots\\' + png2
        im = Image.open(fo)
        img = im.crop((left*dpr,top*dpr,right*dpr,height*dpr))
        img.save(fo2)
        self.dr.close()
        print(pytesseract.image_to_string(Image.open(fo2)))

    def test02(self):
        img=r'C:\Users\ljy\Desktop\MyDemo\PythonDemo\my_selenium\screenshots\2.jpg'
        pytesseract.pytesseract.tesseract_cmd = r"D:\software\Tesseract-OCR\tesseract.exe"
        print(pytesseract.image_to_string(img))



if __name__ == '__main__':
    tc = TestCase()
    tc.test02()