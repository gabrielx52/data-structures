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


    # tests for decimal & negatives