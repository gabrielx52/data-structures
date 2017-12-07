"""Singly linked list data structure."""


class Node(object):
    """Make node object class."""

    def __init__(self):
        """Make node object class."""
        self.data = None
        self.next = None


class LinkedList(object):
    """Make linked list class."""

    def __init__(self, iterable=()):
        """Make linked list object."""
        self.head = None
        self._count = 0
        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)

    def push(self, val):
        """Push a new node on head of linked list."""
        new_node = Node()
        new_node.data = val
        new_node.next = self.head
        self.head = new_node
        self._count += 1

    def pop(self):
        """Remove and return the head item of linked list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list.')
        pop_node = self.head
        self.head = pop_node.next
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
            current_node = current_node.next
        return

    def remove(self, node):
        """Remove node from linked list."""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node == node:
                if previous_node:
                    previous_node.next = current_node.next
                    current_node.next = None
                    self._count -= 1
                else:
                    current_node.next = None
                    self._count -= 1
            previous_node = current_node
            current_node = previous_node.next
        return

    def display(self):
        """Display the linked list value as if a tuple."""
        display_str = ""
        current_head = self.head
        while current_head:
            display_str = "'" + str(current_head.data) + "', " + display_str
            current_head = current_head.next
        return "(" + display_str[:-2] + ")"

    def __str__(self):
        """Print the display."""
        return self.display()


def partition(ll, value):
    """Partition a linked list on value."""
    current = ll.head
    less_vals = []
    great_vals = []
    val = []
    while current:
        if current.data > value:
            great_vals.insert(0, current.data)
        if current.data < value:
            less_vals.insert(0, current.data)
        if current.data == value:
            val.insert(0, value)
        current = current.next
    less_vals.extend(val)
    less_vals.extend(great_vals)
    return LinkedList(less_vals)


def add_two_ll(ll1, ll2):
    """Add two linked lists and return ll with sum."""
    list1 = []
    list2 = []
    current1 = ll1.head
    current2 = ll2.head
    while current1:
        list1.append(current1.data)
        current1 = current1.next
    while current2:
        list2.append(current2.data)
        current2 = current2.next
    list1 = int(''.join([str(i) for i in list1])).reverse()
    list2 = int(''.join([str(i) for i in list2])).reverse()
    llsum = list1 + list2
    return llsum
