"""Implement bubble sort."""


def bubble_sort(alist):
    """Implement a bubble sort."""
    potato = True
    while potato:
        potato = False
        for idx in range(len(alist) - 1):
            if alist[idx] > alist[idx + 1]:
                temp = alist[idx]
                alist[idx] = alist[idx + 1]
                alist[idx + 1] = temp
                potato = True
    return alist

if __name__ == '__main__':
    print('A list: [4, 3, 7, 6] using bubble sort')
    alist = [4, 3, 7, 6]
    print(bubble_sort(alist))
