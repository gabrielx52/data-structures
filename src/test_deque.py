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


def test_peek():
    """Test to see value of last, tail, object with peek()."""
    from deque import Deque
    dq = Deque()
    dq.append('one')
    assert dq.peek() == 'one'


def test_peekleft():
    """Test to see value of first, head, object with peekleft()."""
    from deque import Deque
    dq = Deque()
    dq.append('one')
    dq.append('two')
    assert dq.peekleft() == 'one'


def test_dq_size():
    """Test size method of deque."""
    from deque import Deque
    dq = Deque()
    dq.append(1)
    dq.appendleft(0)
    dq.append(17)
    assert dq.size() == 3
