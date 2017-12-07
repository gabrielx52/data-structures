"""Implement bubble sort."""


def bubble_sort(alist):
    """Implement a bubble sort."""
    data_list = len(alist)
    potato = True
    while potato:
        potato = False
        for i in range(len(alist - 1)):
            if alist[i - 1] > alist[i]:
                temp = alist[i]
                alist[i] = alist[i - 1]
                alist[i - 1] = temp

        potato = True
    break
    return alist

# if __name__ == ‘__main__’:
