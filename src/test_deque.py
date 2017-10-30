"""Test script for deque module."""


def test_deque_object_type():
    """Test instance of type has type deque."""
    from deque import Deque
    dq = Deque()
    assert type(dq) == Deque


def test_append():
    """Test adding to end (append) on deque object."""
    from deque import Deque
    dq = Deque()
    assert dq.append('one') == 'one'
