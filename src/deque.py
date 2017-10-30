"""Implement a deque with methods append, -left, pop, -left, peek, -left."""

from doubly_linked_list import DoublyLinkedList


class Deque(object):
    """Deque object class."""

    def __init__(self):
        """Init new deque instance."""
        self._deque = DoublyLinkedList()
