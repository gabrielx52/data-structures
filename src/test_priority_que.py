"""Test for test_priority que."""
import pytest


def test_priority_que():
    """Test priority_que produces an instance of Priorityq."""
    from priority_que import Priorityq
    pq = Priorityq()
    assert isinstance(pq, Priorityq)


def test_insert():
    """."""
    from priority_que import Priorityq
    pq = Priorityq()
    pq.insert(8)
    assert pq._q == {0: [8]}


def test_insert_error_handling_non_int():
    """."""
    from priority_que import Priorityq
    pq = Priorityq()
    with pytest.raises(TypeError):
        pq.insert(8, 'one')
