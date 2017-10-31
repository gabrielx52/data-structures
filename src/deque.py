"""Implement a deque with methods append, -left, pop, -left, peek, -left."""

from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Deque object class."""

    def __init__(self):
        """Init new deque instance."""
        self._deque = DoublyLinkedList()

    def append(self, val):
        """Add item to right end of deque."""
        self._deque.append(val)

    def appendleft(self, val):
        """Add item to left end of deque."""
        self._deque.push(val)

    def pop(self):
        """Remove item from right end of deque."""
        try:
            return self._deque.shift()
        except IndexError:
            raise IndexError('Cannot pop from empty deque.')

    def popleft(self):
        """Remove item from head, left-side, of deque."""
        try:
            return self._deque.pop()
        except IndexError:
            raise IndexError('Cannot pop from empty deque')

    def peek(self):
        """Show data of item at back of deque."""
        try:
            return self._deque.tail.data
        except AttributeError:
            return None

    def peekleft(self):
        """Show data of item at front of deque."""
        try:
            return self._deque.head.data
        except AttributeError:
            return None

    def size(self):
        """Return the size of the deque."""
        return self._deque._len

    def __len__(self):
        """Return the size of the deque with len."""
        return len(self._deque)
