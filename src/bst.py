"""Implement binary search tree methods.

Hat tip: http://www.laurentluce.com/posts/binary-search-tree-library-in-python/
AND: Magnus Lie Hetlund Algorithms: Mastering Basic Algorithms in the Python/
Language
."""


class Node(object):
    """Node for binary search tree data structure."""

    def __init__(self, val):
        """Initialize node for binary search tree."""
        self.left = None
        self.right = None
        self.value = val


class BST(object):
    """Create binary search tree data structure."""

    def __init__(self, iterable=None):
        """Initiatalize the BST."""
        self.root = None
        self.depth = 0
        self._size = 0
        if iterable:
            if isinstance(iterable, (list, tuple, set)):
                for item in iterable:
                    self.insert.item
                else:
                    raise TypeError('Iterable must be list, tuple, or set')

    def insert(self, val):
        """Insert node into binary search tree."""
        if self.root:
            curr = self.root
            while True:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                else:
                    curr.right = Node(val)
                    self._size += 1
                    return
                if val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(val)
                        self._size += 1
                        return
                if val == curr.val:
                    return
        else:
            self.root = Node(val)
            self._size += 1
            return

    def search(self, val):
        """."""
        if self.root is None:
            raise KeyError
        else:
            curr = self.root
            while True:
                if val > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        raise ValueError('No such value in tree')
                elif val < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        raise ValueError('No such value in tree')
                elif val == curr.val:
                    return curr


    def size(self):
        """Return the size of BST."""
        return self._size

    def depth(self):
        """Return depth of BST."""

    def _contains_(self, val):
        """Return whether node or not."""
        try:
            self.search(val)
        except KeyError:
            return False
        return True

    def balance(self):
        """Balance node returns int, positive or negative."""
