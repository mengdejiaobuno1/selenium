import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (1, 1, 1, 1)
str_to_try = [Task(2, 2, 2, 2),
              Task(3, 3, 3, 3),
              Task(4, 4, 4, 4),
              Task(5, 5, 5, 5)]

@pytest.fixture(params=str_to_try)
def a_task(request):
    """Demonstrate paramertrize with one parameter"""
    print('***************', request.param)
    return request.param

def test_add_a(a_task):
    assert a_task == Task(3,3,3,3)