"""Insert sort test module."""
from random import randrange, sample

import pytest


TEST_CASE = []
for i in range(20):
    x = list(range(randrange(100)))
    TEST_CASE.append((sample(x, len(x)), x))


def test_insert_sort_sorts_small_list():
    """Test that insert sort sorts small list."""
    from insert import insert_sort
    assert insert_sort([4, 10, 7, 1, 9]) == [1, 4, 7, 9, 10]


def test_insert_sort_sorts_big_list():
    """Test that insert sort sorts big list."""
    from insert import insert_sort
    from random import shuffle
    big_list = list(range(100))
    shuffle(big_list)
    assert insert_sort(big_list) == list(range(100))


@pytest.mark.parametrize('unsorted_l, sorted_l', TEST_CASE)
def test_insert_sort_with_medium_lists(unsorted_l, sorted_l):
    """Test insert sort with medium lists."""
    from insert import insert_sort
    assert insert_sort(unsorted_l) == sorted_l


def test_insert_sort_raises_type_error_if_input_not_list():
    """Test that insert sort will raise an error if input not a list."""
    with pytest.raises(TypeError):
        from insert import insert_sort
        insert_sort((1, 2, 4, 3))


def test_insert_sort_n_2_list():
    """Test insert sort works on descending value list."""
    from insert import insert_sort
    assert insert_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6]


def test_insert_sort_on_empty_list():
    """Test insert sort returns empty list on empty list."""
    from insert import insert_sort
    assert insert_sort([]) == []


def test_insert_sort_on_one_item_list():
    """Test insert sort with single item list."""
    from insert import insert_sort
    assert insert_sort([5]) == [5]


def test_insert_sort_on_list_of_letters():
    """Test insert sort with list of letters."""
    from insert import insert_sort
    assert insert_sort(['b', 'f', 'p', 's', 'a']) == ['a', 'b', 'f', 'p', 's']
