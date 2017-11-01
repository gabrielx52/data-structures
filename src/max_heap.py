"""Implement max heap abstract structure."""


class MaxHeap(object):
    """Binary max heap data structure."""

    def __init__(self):
        """Max heap init."""
        self._heap = []

    def push(self, val):
        """Add data to heap."""
        self._heap.append(val)
