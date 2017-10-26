"""Stack data structure."""
from linked_list import LinkedList


class Stack(object):
    """Stack object class."""

    def __init__(self, iterable=()):
        """Init new stack instance."""
        self.ll = LinkedList(iterable)

    def push(self, val):
        """Push new item on stack."""
        self.ll.push(val)
