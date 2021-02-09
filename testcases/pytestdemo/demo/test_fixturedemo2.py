# fixture使用案例scope="class"
import pytest


@pytest.fixture(scope="class")
def fixture_for_class():
    print('用在测试类上的fixture')


# 当加上scope="class"时，当前模块下的所有类，都会调一次fixture，autouse=False时记得传参
def test_1():
    print('执行了测试用例test_1')


def test_2(fixture_for_class):
    print('执行了测试用例test_2')


# 测试类上的fixture'也可以在函数上执行
def test_3():
    print('执行了测试用例test_3')


class Test_Demo1():
    def test_4(self, fixture_for_class):
        print("执行了测试test4")


class Test_Demo2():
    def test_5(self):
        print("执行了测试test5")


if __name__ == "__main__":
    pytest.main(["-s", "test_fixturedemo2.py"])