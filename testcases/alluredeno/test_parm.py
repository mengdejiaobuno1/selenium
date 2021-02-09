import allure
import pytest


@allure.feature("parametrize 测试")
class TestParametrize():

    @pytest.fixture()
    def login(self, request):
        """登录"""
        param = request.param
        print(f"账号是：{param['username']}，密码是：{param['pwd']}")
        # 返回
        return {"code": 0, "msg": "success!"}

    datas = [
        {"username": "name1", "pwd": "pwd1"},
        {"username": "name2", "pwd": "pwd2"},
        {"username": "name3", "pwd": "pwd3"}
    ]

    @allure.story('登录功能')
    @pytest.mark.parametrize('login', datas, indirect=True)
    def test_login1(self, login):
        """
        登录测试用例1
        """
        assert login['code'] == 0

    @allure.story('登录功能')
    @allure.title('登录测试用例2')
    @pytest.mark.parametrize('login', datas, indirect=True)
    def test_login2(self, login):
        """
        登录测试用例2
        """
        assert login['code'] == 0

    ids = [
        "username is name1,pwd is pwd1",
        "username is name2,pwd is pwd2",
        "username is name3,pwd is pwd3"
    ]

    @allure.story('登录功能')
    @pytest.mark.parametrize('login', datas, ids=ids, indirect=True)
    def test_login3(self, login):
        """
        登录测试用例3
        """
        assert login['code'] == 0

    data2 = [
        ("name1", "123456"),
        ("name2", "123456"),
        ("name3", "123456")
    ]
