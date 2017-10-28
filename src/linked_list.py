"""Singly linked list data structure."""


class Node(object):
    """Make node object class."""

    def __init__(self, data, next_node):
        """Make node object class."""
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """Make linked list class."""

    def __init__(self, iterable=None):
        """Make linked list object."""
        self.head = None
        self._count = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Push a new node on head of linked list."""
        self.head = Node(val, self.head)
        self._count += 1

    def pop(self):
        """Remove and return the head item of linked list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list.')
        pop_node = self.head
        self.head = pop_node.next_node
        self._count -= 1
        return pop_node.data

    def size(self):
        """Return size of linked list."""
        return self._count

    def __len__(self):
        """Return length of linked list with len function."""
        return self._count

    def search(self, val):
        """Return node containing value in list if present otherwise None."""
        current_node = self.head
        while current_node:
            if current_node.data == val:
                return current_node
            current_node = current_node.next_node
        return

    def remove(self, node):
        """Remove node from linked list."""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node == node:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                    current_node.next_node = None
                    self._count -= 1
                else:
                    current_node.next_node = None
                    self._count -= 1
            previous_node = current_node
            current_node = previous_node.next_node
        return

    def display(self):
        """Display the linked list value as if a tuple."""
        display_string = ""
        current_head = self.head
        while current_head:
            display_string = "'{}', {}".format(str(current_head.data),
                                               display_string)
            current_head = current_head.next_node
        return "(" + display_string[:-2] + ")"

    def __str__(self):
        """Print the display."""
        return self.display()
