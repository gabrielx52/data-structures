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

    def append(self, val):
        """Append to tail of doubly linked list."""
        new_node = Node()
        new_node.data = val
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self._len += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self._len += 1

    def pop(self):
        """Pop from the head of doubly linked list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list')
        pop_node = self.head
        self.head = pop_node.next
        self.head.prev = None
        self._len -= 1
        return pop_node.data

    def shift(self):
        """Shift from the tail of doubly linked list."""
        if not self.tail:
            raise IndexError('Cannot shift from empty list')
        shift_node = self.tail
        self.tail = shift_node.prev
        self.tail.next = None
        self._len -= 1
        return shift_node.data

    def __len__(self):
        """Python len function will return length of dll."""
        return self._len

    def remove(self, val):
        """Remove node from doubly linked list."""
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == val:
                if previous_node:
                    previous_node.next = current_node.next
                    current_node.next.prev = current_node.prev
                    current_node.next = None
                    current_node.prev = None
                    self._len -= 1
                    return
                else:
                    current_node.next = None
                    current_node.next.prev = None
                    self._len -= 1
                    return
            previous_node = current_node
            current_node = previous_node.next
        raise ValueError("{} not in list".format(val))
