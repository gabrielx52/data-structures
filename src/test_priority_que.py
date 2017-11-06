"""Test for test_priority que."""
import pytest


@pytest.fixture
def empty_que():
    """Empty priority queue fixture."""
    from priority_que import Priorityq
    pq = Priorityq()
    return pq


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


def test_insert_error_handling_non_int(empty_que):
    """."""
    with pytest.raises(TypeError):
        empty_que.insert(8, 'one')


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


def test_pop_index_error_on_empty_queue(empty_que):
    """Test that pop on an empty queue raises Index Error."""
    with pytest.raises(IndexError):
        empty_que.pop()


def test_peek_index_error_on_empty_queue(empty_que):
    """Test that peek on an empty queue raises Index Error."""
    with pytest.raises(IndexError):
        empty_que.peek()
