import pytest


# 预期测试失败，并且确实失败。使用@pytest.mark.xfail()指定你认为会失败的测试用例。
# @pytest.mark.xfail('1'=='2',reason="跳过的原因")
@pytest.mark.xfail(reason="跳过的原因")
def test_passing():
    assert '1' == '12'


@pytest.mark.parametrize("str", ["abc", "def", "twq", "tre"])
def test_add_2(str):
    """Demonstrate paramertrize with one parameter"""
    str2 = "abc"
    assert str == str2
