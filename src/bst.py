"""Binary search tree."""


class Node(object):
    """BST Node object class."""

    def __init__(self, val):
        """Constructor method for BST Node."""
        self.val = val
        self.left = None
        self.right = None


class BST(object):
    """Binary search tree object class."""

    def __init__(self, iterable=None):
        """Constructor method for BST."""
        self._root = None
        self._size = 0
        self._depth = 0
        self._balance = 0
        if iterable:
            if isinstance(iterable, (list, set)):
                for item in iterable:
                    self.insert(item)
            else:
                raise TypeError('Iterable must be a list or set.')

    def insert(self, val):
        """Insert value into BST."""
        if isinstance(val, (int, float)):
            if self._root is None:
                self._root = Node(val)
                self._size += 1
                return
            deep = 0
            current = self._root
            if val > self._root.val:
                self._balance -= 1
            else:
                self._balance += 1
            while True:
                if val > current.val:
                    deep += 1
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        self._size += 1
                        self.depth_checker(deep)
                        return
                if val < current.val:
                    deep += 1
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        self._size += 1
                        self.depth_checker(deep)
                        return
                if val == current.val:
                    return
        else:
            raise TypeError('Node value must be float or int.')

    def depth_checker(self, depth):
        """Compare and update current depth with node depth."""
        if depth > self._depth:
            self._depth = depth

    def search(self, val):
        """Return node containing val."""
        current = self._root
        try:
            if val == current.val:
                return current
            while True:
                if val > current.val:
                    if current.right:
                        current = current.right
                    else:
                        return None
                if val < current.val:
                    if current.left:
                        current = current.left
                    else:
                        return None
                if val == current.val:
                    return current
        except AttributeError:
            return

    def size(self):
        """Return size of BST."""
        return self._size

    def depth(self):
        """Return depth of BST."""
        return self._depth

    def contains(self, val):
        """Return True/False if val is in BST."""
        return bool(self.search(val))

    def balance(self):
        """Return True/False if BST is balanced."""
        return self._balance
