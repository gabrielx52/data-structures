"""Radix sort."""


def radix_sort(seq):
    """Radix sort function."""
    if not seq:
        return []
    if isinstance(seq, list):
        buckets = {x: [] for x in range(10)}
        max_sorts = len(str(max(seq)))
        seq = [str(num) for num in seq]
        for j, num in enumerate(seq):
            if len(num) < max_sorts:
                seq[j] = '0' * (max_sorts - len(num)) + num
        for i in range(max_sorts)[::-1]:
            hold = []
            for num in seq:
                buckets[int(num[i])].append(num)
            for buck in buckets:
                while len(buckets[buck]) > 0:
                    hold.append(buckets[buck].pop(0))
            seq = hold[:]
        return [int(x) for x in seq]
    else:
        raise TypeError('Input type must be a list.')

if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = [1, 9, 2, 8, 3, 7, 4, 6, 5]
    count = 10000

    time_1 = ti.timeit("radix_sort(list1)",
                       setup="from __main__ import list1, radix_sort",
                       number=count)
    time_2 = ti.timeit("radix_sort(list2)",
                       setup="from __main__ import list2, radix_sort",
                       number=count)
    time_3 = ti.timeit("radix_sort(list3)",
                       setup="from __main__ import list3, radix_sort",
                       number=count)
    print(f"""
Radix sort sorts a list by stepping through it, swapping items
depending on value until no more swaps can be made.

Input:[1, 2, 3, 4, 5, 6, 7, 8, 9]
Sort time: {time_1/count}

Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2/count}

Input:[1, 9, 2, 8, 3, 7, 4, 6, 5]
Sort time: {time_3/count}
        """)