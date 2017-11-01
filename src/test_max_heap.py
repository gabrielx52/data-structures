"""Implement max heap abstract structure tests."""


def test_max_heap():
    """Test instance of MaxHeap."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert isinstance(mh, MaxHeap)


def test_max_heap_push():
    """Test max heap push: add data node to the list."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    mh.push('one')
    assert len(mh._heap) == 1
