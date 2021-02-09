from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

class TestUserRegister():
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get(r'http://localhost:8080/jpress/user/register')
        self.dr.maximize_window()

    def test_register_code_error(self):
        username = 'name'
        email = username + '@qq.com'
        pswd = '123456'
        confirmpswd = '123456'
        yzm = 'xyzc'

        self.dr.find_element_by_name('username').send_keys(username)
        self.dr.find_element_by_name('email').send_keys(email)
        self.dr.find_element_by_name('pwd').send_keys(pswd)
        self.dr.find_element_by_name('confirmPwd').send_keys(confirmpswd)
        self.dr.find_element_by_name('captcha').send_keys(yzm)
        self.dr.find_element_by_class_name('btn').click()

        WebDriverWait(self.dr, 5, 0.5).until(EC.alert_is_present())

        al = self.dr.switch_to.alert
        assert al.text == '验证码不正确'
        al.accept()
        time.sleep(5)
        self.dr.close()




