import pytest

def exc(x):
    if x == 0:
        raise ValueError("value not 0")
    return 2 / x

def test_raises():
    with pytest.raises(ValueError, match="value not \d+$") as exec_info:
        exc(0)
    print("exec_info.type = ", exec_info.type)
    print("exec_info.value.args = ", exec_info.value.args)

    assert exec_info.type == ValueError
    assert exec_info.value.args[0] == "value not 0"

test_raises()