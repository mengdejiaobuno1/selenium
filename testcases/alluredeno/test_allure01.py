import allure
import pytest

@allure.step("步骤1:点xxx")
def step_1():
    print("111")

@allure.step("步骤2:点xxx")
def step_2():
    print("222")

@allure.feature("一级模块")
class TestEditPage():
    '''编辑页面'''

    @allure.story("二级模块一")
    @allure.title("测试用例标题一")
    @allure.severity("critical")
    @allure.description("测试用例描述一")
    def test_1(self):
        '''用例描述：先登录，再去执行xxx'''
        step_1()
        step_2()
        print("xxx")


    @allure.story("二级模块二")
    @allure.title("测试用例标题二")
    @allure.severity("normal")
    @allure.description("测试用例描述二")
    def test_2(self):
        '''用例描述：先登录，再去执行yyy'''
        with allure.step("步骤1"):
            print('1111')
        with allure.step("步骤2"):
            allure.attach('1.txt','公众号',allure.attachment_type.TEXT)
        with allure.step("步骤3"):
            allure.attach.file(r'./1.jpg',"海瑞",allure.attachment_type.JPG)
        with allure.step("步骤4"):
            allure.attach('<head></head><body> 一个HTML页面 </body>', 'Attach with HTML type', allure.attachment_type.HTML)
        print("yyy")