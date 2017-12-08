"""Bubble sort test module."""
from random import randrange, sample

import pytest


TEST_CASE = []
for i in range(20):
    x = list(range(randrange(100)))
    TEST_CASE.append((sample(x, len(x)), x))


def test_bubble_sort_sorts_small_list():
    """Test that bubble sort sorts small list."""
    from bubble import bubble_sort
    assert bubble_sort([4, 10, 7, 1, 9]) == [1, 4, 7, 9, 10]


def test_bubble_sort_sorts_big_list():
    """Test that bubble sort sorts big list."""
    from bubble import bubble_sort
    from random import shuffle
    big_list = list(range(100))
    shuffle(big_list)
    assert bubble_sort(big_list) == list(range(100))


@pytest.mark.parametrize('unsorted_l, sorted_l', TEST_CASE)
def test_bubble_sort_with_medium_lists(unsorted_l, sorted_l):
    """Test bubble sort with medium lists."""
    from bubble import bubble_sort
    assert bubble_sort(unsorted_l) == sorted_l


def test_bubble_sort_raises_type_error_if_input_not_list():
    """Test that bubble sort will raise an error if input not a list."""
    with pytest.raises(TypeError):
        from bubble import bubble_sort
        bubble_sort((1, 2, 4, 3))


def test_bubble_sort_n_2_list():
    """Test bubble sort works on descending value list."""
    from bubble import bubble_sort
    assert bubble_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]


def test_bubble_sort_on_empty_list():
    """Test bubble sort returns empty list on empty list."""
    from bubble import bubble_sort
    assert bubble_sort([]) == []


def test_bubble_sort_on_one_item_list():
    """Test bubble sort with single item list."""
    from bubble import bubble_sort
    assert bubble_sort([5]) == [5]


def test_bubble_sort_on_list_of_letters():
    """Test bubble sort with list of letters."""
    from bubble import bubble_sort
    assert bubble_sort(['b', 'f', 'p', 's', 'a']) == ['a', 'b', 'f', 'p', 's']
