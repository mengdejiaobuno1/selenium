import pytest


def test_a():
    print("test_a")

class TestDemo():
    @pytest.mark.slow
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        a = 'hello'
        b = 'hello world'
        assert a not in b

class TestDemo1():
    def test_one(self):
        print("开始执行 test_one 方法")

        a = 'hello'
        b = 'hello world'
        assert a not in b

    def test_o2(self):
        print("开始执行 test_o2 方法")
        x = 'this'
        assert 'h' in x

    def test_3(self):
        print("开始执行 test_3 方法")
        x = 'hello'
        assert 'e' in x
