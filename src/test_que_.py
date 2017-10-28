"""Test the que_.py."""


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
    assert q.dequeue == 'one'
