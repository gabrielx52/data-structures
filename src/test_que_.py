"""Test the que_.py."""
import pytest


def test_enqueue_method():
    """Add a node into the queue."""
    from que_ import Queue
    q = Queue()
    assert type(q) == Queue


def test_dequeue_method():
    """Remove a node in the proper sequence."""
    from que_ import Queue
    q = Queue()
    q.enqueue('one')
    q.enqueue('two')
    assert q.dequeue() == 'one'


def test_dequeue_raise_index_error():
    """Raise an indext error when list empty."""
    from que_ import Queue
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()


def test_queue_peek_with_data():
    """Test the queue peek method displays the tail."""
    from que_ import Queue
    q = Queue()
    q.enqueue('one')
    q.enqueue('two')
    assert q.peek() == 'one'


def test_queue_peek_with_no_data():
    """Test the queue peek returns None."""
    from que_ import Queue
    q = Queue()
    assert q.peek() is None


def test_queue_size_method():
    """Test that queue size method returns size."""
    from que_ import Queue
    q = Queue()
    q.enqueue('one')
    q.enqueue('two')
    assert q.size() == 2


def test_queue_len_function():
    """Test that len function returns queue size."""
    from que_ import Queue
    q = Queue()
    q.enqueue('one')
    q.enqueue('two')
    assert len(q) == 2
