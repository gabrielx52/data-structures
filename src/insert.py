"""Insert sort module."""


def insert_sort(l):
    """Sort a list of numbers by insert sort."""
    for i in range(len(l) - 1):
        for j in range(i + 1, 0, -1):
            if l[j] < l[j - 1]:
                tmp = l[j]
                l[j] = l[j - 1]
                l[j - 1] = tmp
    return l
