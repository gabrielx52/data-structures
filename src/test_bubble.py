"""Test bubble sort implementation."""
from bubble import bubble_sort


def test_bubble_sort_short_list():
    """Test bubble with small list."""
    short_list = [4, 3, 7, 6]
    assert bubble_sort(short_list) == [3, 4, 6, 7]
