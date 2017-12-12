"""Quick sort."""


def quick_sort(seq):
    """Quicksort method."""
    if isinstance(seq, list):
        if len(seq) <= 1:
            return seq
        piv, seq = seq[0], seq[1:]
        low, high = [x for x in seq if x <= piv], [x for x in seq if x > piv]
        return quick_sort(low) + [piv] + quick_sort(high)
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))
    count = 10000

    time_1 = ti.timeit("quick_sort(list1[:])",
                       setup="from __main__ import list1, quick_sort",
                       number=count)
    time_2 = ti.timeit("quick_sort(list2[:])",
                       setup="from __main__ import list2, quick_sort",
                       number=count)
    time_3 = ti.timeit("quick_sort(list3[:])",
                       setup="from __main__ import list3, quick_sort",
                       number=count)
    print(f"""
Quick sort sorts a list by stepping through it, swapping items
depending on value until no more swaps can be made.

Input:[1, 2, 4, 6]
Sort time: {time_1/count}

Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2/count}

Input:list(range(100, 0, -1))
Sort time: {time_3/count}
        """)

