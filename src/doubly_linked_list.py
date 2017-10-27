"""Doubly linked list data structures."""


class Node(object):
    """Make the node object."""

    def __init__(self):
        """Make node object class."""
        self.data = None
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    """Make doubly linked list object."""

    def __init__(self):
        """Doubly linked list class object."""
        self.head = None
        self.tail = None
        self._len = 0

    def push(self, val):
        """Push doubly linked list."""
        new_node = Node()
        new_node.data = val
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self._len += 1
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self._len += 1
