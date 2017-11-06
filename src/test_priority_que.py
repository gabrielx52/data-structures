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


def test_peek_method_shows_highest_priority():
    """Peek method returns highest priority item in queue."""
    from priority_que import Priorityq
    pq = Priorityq()
    pq.insert(1)
    pq.insert(4)
    pq.insert(2, 2)
    pq.insert(3)
    assert pq.peek() == 2


def test_pop_method_shows_most_important_value():
    """Test the pop method returns highest priority value."""
    from priority_que import Priorityq
    pq = Priorityq()
    pq.insert(1)
    pq.insert(4)
    pq.insert(2, 2)
    pq.insert(3)
    assert pq.pop() == 2
