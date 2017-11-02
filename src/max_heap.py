"""Implement max heap abstract structure."""


class MaxHeap(object):
    """Binary max heap data structure."""

    def __init__(self, iterable=None):
        """Max heap init."""
        self._heap = []
        if isinstance(iterable, (tuple, list)):
            for item in iterable:
                self.push(item)

    def __len__(self):
        """Return the length of the heap."""
        return len(self._heap)

    def push(self, val):
        """Add data to heap."""
        if type(val) == int:
            if val in self._heap:
                raise ValueError('Cannot have duplicate values in list')
            if not self._heap:
                self._heap.append(val)
            else:
                self._heap.append(val)
                self._sort(len(self._heap) - 1)
        else:
            raise TypeError('Must add an integer')

    def parent(self, i):
        """Return index of parent node."""
        return (i - 1) // 2

    def _sort(self, i):
        """Sort the heap."""
        n_idx = i
        p_idx = self.parent(i)
        if self._heap[n_idx] > self._heap[p_idx]:
            tmp = self._heap[i]
            self._heap[n_idx] = self._heap[p_idx]
            self._heap[n_idx] = self._heap[p_idx]
            self._heap[p_idx] = tmp
            if p_idx:
                self._sort(p_idx)
            else:
                return
        else:
            return

    def pop(self):
        """Pop the top value and resort the heap according to precedence."""
        try:
            top_node = self._heap[0]
            self._heap = [self._heap[-1]] + self._heap[1:-1]
            self.sort_down(0)
            return top_node
        except IndexError:
            raise IndexError('Cannot pop from an empty heap')

    def sort_down(self, i):
        """Sort after a pop."""
        while ((i + 1) * 2) <= len(self._heap) + 1:
            mc = self.max_child(i)
            if self._heap[i] < self._heap[mc]:
                tmp = self._heap[i]
                self._heap[i] = self._heap[mc]
                self._heap[mc] = tmp
            i = mc

    def max_child(self, i):
        """Return the max child."""
        if (i * 2) + 2 > len(self._heap):
            return (i * 2) + 1
        else:
            if self._heap[(i * 2) + 1] > self._heap[(i * 2) + 2]:
                return (i * 2) + 1
            else:
                return (i * 2) + 2
