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
        """See the highest priority key and its first in value."""
        if self._q:
            return self._q[max(self._q.keys())][0]

    def pop(self):
        """Remove and return highest priority item."""
        if self._q:
            vip = max(self._q.keys())
            if len(self._q[vip]) > 1:
                return self._q[vip].pop(0)
            elif len(self._q[vip]) == 1:
                node = self.peek()
                del self._q[vip]
                return node
        raise IndexError('Cannot pop for empty queue')
