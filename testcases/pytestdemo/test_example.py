# fixture使用案例scope="function"
import pytest


@pytest.fixture(scope="class")
def fixture_for_func():
    print('这是fixture装饰器标记的函数')


def test_1():
    print('执行了测试用例test_1')


def test_2():
    print('执行了测试用例test_2')


def test_3(fixture_for_func):
    print('执行了测试用例test_3')


class Test_Demo1():
    def test_4(self, fixture_for_class):
        print("执行了测试test4")


class Test_Demo2():
    def test_5(self):
        print("执行了测试test5")


if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_example.py"])