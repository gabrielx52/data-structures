"""Implement max heap abstract structure."""


class MaxHeap(object):
    """Binary max heap data structure."""

    def __init__(self):
        """Max heap init."""
        self._heap = []

    def push(self, val):
        """Add data to heap."""
        if not self._heap:
            self._heap.append(val)
        else:
            self._heap.append(val)
            self.sort(len(self._heap) - 1, val)

    def parent(self, i):
        """Return index of parent node."""
        return (i - 1) // 2

    def left_child(self, i):
        """Return index of left child node."""
        return 2 * i + 1

    def right_child(self, i):
        """Return index of right child node."""
        return 2 * i + 1

    def sort(self, i, val):
        """Sort the heap."""
        n_idx = i
        p_idx = self.parent(i)
        if self._heap[n_idx] > self._heap[p_idx]:
            self._heap[n_idx] = self._heap[p_idx]
            self._heap[n_idx] = self._heap[p_idx]
            self._heap[p_idx] = val
            if p_idx:
                self.sort(p_idx, val)
            else:
                return
        else:
            return
