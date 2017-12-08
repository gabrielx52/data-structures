"""Insert sort module."""


def insert_sort(l):
    """Sort a list of numbers by insert sort."""
    if isinstance(l, list):
        for i in range(len(l) - 1):
            for j in range(i + 1, 0, -1):
                if l[j] < l[j - 1]:
                    tmp = l[j]
                    l[j] = l[j - 1]
                    l[j - 1] = tmp
        return l
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))

    time_1 = ti.timeit("insert_sort(list1)",
                       setup="from __main__ import list1, insert_sort")
    time_2 = ti.timeit("insert_sort(list2)",
                       setup="from __main__ import list2, insert_sort")
    time_3 = ti.timeit("insert_sort(list3)",
                       setup="from __main__ import list3, insert_sort")
    print(f"""
Insert sort sorts a list by stepping through it, swapping items
depending on value until no more swaps can be made.

Input:[1, 2, 4, 6]
Sort time: {time_1}

Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2}

Input:list(range(100, 0, -1))
Sort time: {time_3}
        """)
