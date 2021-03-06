"""Bubble sort algorithm."""


def bubble_sort(l):
    """Sort a list of numbers by bubble sort."""
    if isinstance(l, list):
        swap = 1
        while swap:
            swap = 0
            for i in range(len(l) - 1):
                if l[i] > l[i + 1]:
                    tmp = l[i]
                    l[i] = l[i + 1]
                    l[i + 1] = tmp
                    swap += 1
            if swap == 0:
                return l
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))

    time_1 = ti.timeit("bubble_sort(list1)",
                       setup="from __main__ import list1, bubble_sort")
    time_2 = ti.timeit("bubble_sort(list2)",
                       setup="from __main__ import list2, bubble_sort")
    time_3 = ti.timeit("bubble_sort(list3)",
                       setup="from __main__ import list3, bubble_sort")
    print(f"""
Bubble sort sorts a list by stepping through it, swapping items
depending on value until no more swaps can be made.

Input:[1, 2, 4, 6]
Sort time: {time_1}

Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2}

Input:list(range(100, 0, -1))
Sort time: {time_3}
        """)
