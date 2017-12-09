"""Test bubble sort implementation."""
from bubble import bubble_sort


def test_bubble_sort_short_list():
    """Test bubble with small list."""
    short_list = [4, 3, 7, 6]
    assert bubble_sort(short_list) == [3, 4, 6, 7]


def test_bubble_sort_long_list():
    """Test bubble with long list."""
    long_list = [72, 4, 10, 6, 20, 18, 91, 45, 3, 15]
    assert bubble_sort(long_list) == [3, 4, 6, 10, 15, 18, 20, 45, 72, 91]


def test_bubble_sort_negative_num():
    """Test bubble sort works with negative numbers."""
    list_negative_num = [72, 4, -6]
    assert bubble_sort(list_negative_num) == [-6, 4, 72]


def test_bubble_sort_decimals():
    """Test bubble sort takes a decimal float."""
    list_decimals = [5.5, 5.3, 5.2, 4]
    assert bubble_sort(list_decimals) == [4, 5.2, 5.3, 5.5]

    # tests for decimal