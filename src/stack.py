"""Stack data structure."""
from linked_list import LinkedList


class Stack(object):
    """Stack object class."""

    def __init__(self, iterable=()):
        """Init new stack instance."""
        self.ll = LinkedList(iterable)
        self._count = 0

    def push(self, val):
        """Push new item on stack."""
        self.ll.push(val)
        self._count += 1

    def pop(self):
        """Pop last-in item on stack."""
        pop_node = self.ll.pop()
        self._count -= 1
        return pop_node

    def __len__(self):
        """Return size of stack with len() function."""
        return self._count
