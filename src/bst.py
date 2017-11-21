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
        self.size = 0
        self.depth = 0
        self.balance = 0

    def insert(self, val):
        """Insert value into BST."""
        if self.root is None:
            self.root = Node(val)
            self.size += 1
            return
        current = self.root
        while True:
            if val > current.val:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    self.size += 1
                    return
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    self.size += 1
                    return
            if val == current.val:
                return

    def search(self, val):
        """Return node containing val."""

    def size(self):
        """Return size of BST."""
        return self.size

    def depth(self):
        """Return depth of BST."""
        return self.depth

    def contains(self, val):
        """Return True/False if val is in BST."""

    def balance(self):
        """Return True/False if BST is balanced."""
        return self.balance == 0
