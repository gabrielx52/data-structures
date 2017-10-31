"""Implement max heap abstract structure tests."""


def test_max_heap():
    """Test instance of MaxHeap."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert isinstance(mh, MaxHeap)
