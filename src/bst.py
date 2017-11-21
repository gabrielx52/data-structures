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
        self.iter = iterable
        self.root = None
        self._size = 0
        self.depth = 0
        self.balance = 0

    def insert(self, val):
        """Insert value into BST."""
        if self.root is None:
            self.root = Node(val)
            self._size += 1
            return
        deep = 0
        current = self.root
        if val > self.root.val:
            self.balance -= 1
        else:
            self.balance += 1
        while True:
            if val > current.val:
                if current.right:
                    current = current.right
                    deep += 1
                else:
                    current.right = Node(val)
                    self._size += 1
                    self.depth_checker(deep)
                    return
            if val < current.val:
                if current.left:
                    current = current.left
                    deep += 1
                else:
                    current.left = Node(val)
                    self._size += 1
                    self.depth_checker(deep)
                    return
            if val == current.val:
                return

    def depth_checker(self, depth):
        """Compare and update current depth with node depth."""
        if depth > self.depth:
            self.depth = depth

    def search(self, val):
        """Return node containing val."""
        current = self.root
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

    def size(self):
        """Return size of BST."""
        return self._size

    def depth(self):
        """Return depth of BST."""
        # return self.depth

    def contains(self, val):
        """Return True/False if val is in BST."""
        return bool(self.search(val))

    def balance(self):
        """Return True/False if BST is balanced."""
        return self.balance
