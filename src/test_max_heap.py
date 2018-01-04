"""Implement max heap abstract structure tests."""
import pytest


@pytest.fixture
def empty_heap():
    """Set up empty heap fixture."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    return mh


@pytest.fixture
def full_heap():
    """Set up heap with data."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    mh.push(1)
    mh.push(8)
    mh.push(11)
    mh.push(99)
    mh.push(37)
    mh.push(7)
    mh.push(-1)
    return mh


def test_constructor_accepts_iterable(empty_heap):
    """Test constructor accepts tuples or lists."""
    from max_heap import MaxHeap
    assert isinstance(empty_heap, MaxHeap)


def test_max_heap(empty_heap):
    """Test instance of MaxHeap."""
    from max_heap import MaxHeap
    mh = MaxHeap((1, 8, 11, 99, 37, 7, -1))
    assert mh._heap == [99, 37, 8, 1, 11, 7, -1]


def test_max_heap_push(full_heap):
    """Test max heap push: add data node to the list."""
    assert len(full_heap) == 7


def test_max_heap_push_not_take_float(empty_heap):
    """Test max heap push: raises error for value with float."""
    with pytest.raises(TypeError):
        empty_heap.push(1.00)


def test_value_error_for_non_unique_push(full_heap):
    """Test ValueError raises if push a duplicate value."""
    with pytest.raises(ValueError):
        full_heap.push(99)


def test_max_heap_push_not_take_str(empty_heap):
    """Test max heap push: raises error for string push."""
    with pytest.raises(TypeError):
        empty_heap.push('hello')


def test_max_heap_binary_structure(full_heap):
    """Test max heap push: add data node to the list."""
    assert full_heap._heap == [99, 37, 8, 1, 11, 7, -1]


def test_parent_for_item_in_heap():
    """Test the parent method returns correct parent index."""
    from max_heap import MaxHeap
    mh = MaxHeap()
    assert mh.parent(9) == 4


def test_pop_method(full_heap):
    """Test pop method."""
    assert full_heap.pop() == 99
    assert full_heap.pop() == 37


def test_sort_after_pop(full_heap):
    """Test sort method after a value has been popped."""
    full_heap.pop()
    assert full_heap._heap == [37, 11, 8, 1, -1, 7]


def test_pop_empty_heap_raises_error(empty_heap):
    """Test pop on an empty heap raises IndexError."""
    with pytest.raises(IndexError):
        empty_heap.pop()
