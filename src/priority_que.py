"""Priority queue data structure."""


class Priorityq(object):
    """Priority queue class."""

    def __init__(self):
        """Priority queue constructor method."""
        self._q = {}

    def insert(self, val, weight=0):
        """Insert value into priority queue."""
        if type(weight) != int:
            raise TypeError('Weight must be int type')
        try:
            self._q[weight].append(val)
        except:
            self._q[weight] = [val]

    def peek(self):
        """."""

    def pop(self):
        """."""
