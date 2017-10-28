"""Implement a que to accept methods enqueue, dequeue, peek, and size."""

from doubly_linked_list import DoublyLinkedList


class Queue(object):
    """Queue object class."""

    def __init__(self):
        """Init new queue instance."""
        self._queue = DoublyLinkedList()

    def enqueue(self, value):
        """Add node to queue in sequence."""
        self._queue.push(value)

    def dequeue(self):
        """Remove from end of list in sequence."""
        try:
            return self._queue.shift()
        except IndexError:
            raise IndexError('Cannot dequeue from an empty queue')
