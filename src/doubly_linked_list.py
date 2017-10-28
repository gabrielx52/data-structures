"""Doubly linked list data structures."""


class Node(object):
    """Make the node object."""

    def __init__(self, data, prev=None, next_n=None):
        """Make node object class."""
        self.data = data
        self.prev = prev
        self.next_n = next_n


class DoublyLinkedList(object):
    """Make doubly linked list object."""

    def __init__(self):
        """Doubly linked list class object."""
        self.head = None
        self.tail = None
        self._len = 0

    def push(self, val):
        """Push doubly linked list."""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self._len += 1
        else:
            self.head.prev = new_node
            new_node.next_n = self.head
            self.head = new_node
            self._len += 1

    def append(self, val):
        """Append to tail of doubly linked list."""
        new_node = Node(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            self._len += 1
        else:
            self.tail.next_n = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self._len += 1

    def pop(self):
        """Pop from the head of doubly linked list."""
        if not self.head:
            raise IndexError('Cannot pop from empty list')
        if self.head == self.tail:
            pop_node = self.head
            self.head = self.tail = None
            self._len -= 1
            return pop_node.data
        pop_node = self.head
        self.head = pop_node.next_n
        self.head.prev = None
        self._len -= 1
        return pop_node.data

    def shift(self):
        """Shift from the tail of doubly linked list."""
        if not self.tail:
            raise IndexError('Cannot shift from empty list')
        if self.tail == self.head:
            shift_node = self.tail
            self.tail = self.head = None
            self._len -= 1
            return shift_node.data
        shift_node = self.tail
        self.tail = shift_node.prev
        self.tail.next_n = None
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
                if self.head == self.tail:
                    self.head = self.tail = None
                    self._len -= 1
                    return
                if current_node == self.tail:
                    self.tail.next_n = None
                    current_node.prev = None
                    self._len -= 1
                    return
                if previous_node:
                    previous_node.next_n = current_node.next_n
                    current_node.next_n.prev = current_node.prev
                    current_node.next_n = current_node.prev = None
                    self._len -= 1
                    return
                else:
                    current_node.next_n.prev = current_node.next_n = None
                    self._len -= 1
                    return
            previous_node = current_node
            current_node = previous_node.next_n
        raise ValueError("{} not in list".format(str(val)))
