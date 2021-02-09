from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class TestCase():
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://www.jpress.io/user/register')
        self.dr.maximize_window()
        sleep(5)


    def test02(self):
        ele = self.dr.find_element_by_id('agree')
        ActionChains(self.dr).move_to_element(ele).click().perform()
        sleep(5)
        self.dr.quit()

    def test03(self):
        myrect = self.dr.find_element_by_id('agree').rect
        local = self.dr.find_element_by_id('agree').location
        print(myrect)
        print(local)
        ActionChains(self.dr).move_by_offset(myrect['x'],myrect['y']).click().perform()
        sleep(5)
        self.dr.quit()


if __name__ == '__main__':
    tc = TestCase()
    tc.test01()