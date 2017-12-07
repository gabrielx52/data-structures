"""Implement bubble sort."""


def bubble_sort(alist):
    """Implement a bubble sort."""
    num_list = len(alist)
    while True:
        for i in range(num_list):
            if num_list[i - 1] > num_list[i]:
                temp = num_list[i]
                num_list[i] = num_list[i - 1]
                num_list[i - 1] = temp
