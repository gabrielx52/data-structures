"""Merge sort test module."""
from random import randrange, sample

import pytest


TEST_CASE = []
for i in range(20):
    x = list(range(randrange(100)))
    TEST_CASE.append((sample(x, len(x)), x))


def test_merge_sort_sorts_small_list():
    """Test that merge sort sorts small list."""
    from merge import merge_sort
    assert merge_sort([4, 10, 7, 1, 9]) == [1, 4, 7, 9, 10]


def test_merge_sort_sorts_big_list():
    """Test that merge sort sorts big list."""
    from merge import merge_sort
    from random import shuffle
    big_list = list(range(100))
    shuffle(big_list)
    assert merge_sort(big_list) == list(range(100))


@pytest.mark.parametrize('unsorted_l, sorted_l', TEST_CASE)
def test_merge_sort_with_medium_lists(unsorted_l, sorted_l):
    """Test merge sort with medium lists."""
    from merge import merge_sort
    assert merge_sort(unsorted_l) == sorted_l


def test_merge_sort_raises_type_error_if_input_not_list():
    """Test that merge sort will raise an error if input not a list."""
    with pytest.raises(TypeError):
        from merge import merge_sort
        merge_sort((1, 2, 4, 3))


def test_merge_sort_n_2_list():
    """Test merge sort works on descending value list."""
    from merge import merge_sort
    assert merge_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]


def test_merge_sort_on_empty_list():
    """Test merge sort returns empty list on empty list."""
    from merge import merge_sort
    assert merge_sort([]) == []


def test_merge_sort_on_one_item_list():
    """Test merge sort with single item list."""
    from merge import merge_sort
    assert merge_sort([5]) == [5]


def test_merge_sort_on_list_of_letters():
    """Test merge sort with list of letters."""
    from merge import merge_sort
    assert merge_sort(['b', 'f', 'p', 's', 'a']) == ['a', 'b', 'f', 'p', 's']
