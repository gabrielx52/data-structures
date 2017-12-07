"""Implement bubble sort."""


def bubble_sort(alist):
    """Implement a bubble sort."""
    while True:
        for i in range(len(alist)):
            if alist[i - 1] > alist[i]:
                temp = alist[i]
                alist[i] = alist[i - 1]
                alist[i - 1] = temp
    return alist

# if __name__ == ‘__main__’:
