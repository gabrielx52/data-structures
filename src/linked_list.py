"""Singly linked list data structure."""


class Node(object):
    """Make node object class."""

    def __init__(self):
        """Make node object class."""
        self.data = None
        self.next = None


class LinkedList(object):
    """Make linked list class."""

    def __init__(self):
        """Make linked list object."""
        self.head = None
        self.count = 0

    def push(self, val):
        """Push a new node on head of linked list."""
        new_node = Node()
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def pop(self):
        """Remove and return the head item of linked list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list.')
        pop_node = self.head
        self.head = pop_node.next
        self.count -= 1
        return pop_node.data

    def size(self):
        """Return size of linked list."""
        return self.count

    def search(self, val):
        """Return node containing value in list if present otherwise None."""
        current_node = self.head
        while current_node:
            if current_node.data == val:
                return current_node
            current_node = current_node.next
        return
