"""Merge sort module."""


def merge_sort(seq):
    """Sort sequence by merge sort."""
    if isinstance(seq, list):
        mid = len(seq) // 2
        left, right = seq[:mid], seq[mid:]
        if len(left) > 1:
            left = merge_sort(left)
        if len(right) > 1:
            right = merge_sort(right)
        sorted_seq = []
        while left and right:
            if left[-1] >= right[-1]:
                sorted_seq.insert(0, left.pop())
            else:
                sorted_seq.insert(0, right.pop())
        return list(left or right) + sorted_seq
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))
    count = 100000

    time_1 = ti.timeit("merge_sort(list1[:])",
                       setup="from __main__ import list1, merge_sort",
                       number=count)
    time_2 = ti.timeit("merge_sort(list2[:])",
                       setup="from __main__ import list2, merge_sort",
                       number=count)
    time_3 = ti.timeit("merge_sort(list3[:])",
                       setup="from __main__ import list3, merge_sort",
                       number=count)
    print(f"""
Merge sort sorts a list by stepping through it, swapping items
depending on value until no more swaps can be made.

Input:[1, 2, 4, 6]
Sort time: {time_1/count}

Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2/count}

Input:list(range(100, 0, -1))
Sort time: {time_3/count}
        """)