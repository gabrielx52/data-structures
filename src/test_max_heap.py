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
    mh.push(1)
    assert len(mh._heap) == 1


def test_max_heap_binary_structure():
    """Test max heap push: add data node to the list."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    mh.push(1)
    mh.push(8)
    mh.push(11)
    assert mh._heap == [11, 1, 8]


def test_parent_for_item_in_heap():
    """Test the parent method returns correct parent index."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert mh.parent(9) == 4
