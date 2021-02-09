import pytest

@pytest.fixture( autouse=False)
def fixture_for_func():
    print('这是fixture装饰器标记的函数')


def test_1():
    print('执行了测试用例test_1')


def test_2():
    print('执行了测试用例test_2')


def test_3(fixture_for_func):
    print('执行了测试用例test_3')


if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_fixturedemo1.py"])