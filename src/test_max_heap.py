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


def test_left_child():
    """Test the left child method returns correct left child index."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert mh.left_child(3) == 7


def test_right_child():
    """Test the right child method returns correct right child index."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert mh.right_child(7) == 16


def test_sort_with_lots_of_pushes():
    """Test sort with lots of data."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    mh.push(1)
    mh.push(8)
    mh.push(11)
    mh.push(99)
    mh.push(37)
    mh.push(7)
    mh.push(-1)
    assert mh._heap == [99, 37, 8, 1, 11, 7, -1]
