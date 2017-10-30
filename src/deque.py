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
