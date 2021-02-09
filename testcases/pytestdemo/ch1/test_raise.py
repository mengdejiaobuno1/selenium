from collections import namedtuple

import pytest
Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)  # 指定默认值
tasks = Task

def test_add_raises():
    """add() should raise an exception with wrong type param"""
    with pytest.raises(TypeError):
        tasks.add(task="not a Task object")