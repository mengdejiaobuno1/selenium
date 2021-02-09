import pytest
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (1, 1, 1, 1)
str_to_try = [Task(2, 2, 2, 2),
              Task(3, 3, 3, 3),
              Task(4, 4, 4, 4),
              Task(5, 5, 5, 5)]

str_ids = ["Task({},{},{},{})".format(i.summary, i.owner, i.done, i.id) for i in str_to_try]
print(str_ids)


@pytest.mark.parametrize("task", str_to_try)
def test_add_2(task):
    """Demonstrate paramertrize with one parameter"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

@pytest.mark.parametrize("task",str_to_try,ids=str_ids)
def test_add_3(task):
    """Demonstrate paramertrize with one parameter"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2