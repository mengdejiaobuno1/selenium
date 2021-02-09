"""Type the Task data type"""
from collections import namedtuple

import pytest

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

@pytest.mark.smoke
def test_asdict():
    """_asdict() should return a dictionary"""
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something',
               'owner': 'okken',
               'done': True,
               'id': 21}
    assert t_dict == expected

@pytest.mark.smoke
@pytest.mark.get
def test_replace():
    """replace() should change passed in fields"""
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected

@pytest.mark.mark1
@pytest.mark.skip(reason="跳过的原因")
def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)