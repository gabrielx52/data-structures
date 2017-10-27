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
