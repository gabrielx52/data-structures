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
    dq.append('one')
    assert dq._deque.head.data == 'one'


def test_appendleft():
    """Test adding to front (appendleft) on deque object."""
    from deque import Deque
    dq = Deque()
    dq.appendleft('one')
    assert dq._deque.head.data == 'one'


def test_pop():
    """Test remove object from front of deque with pop()."""
    from deque import Deque
    dq = Deque()
    dq.append('one')
    assert dq.pop() == 'one'


def test_popleft():
    """Test remove object from end of deque with popleft()."""
    from deque import Deque
    dq = Deque()
    dq.append('one')
    assert dq.popleft() == 'one'
