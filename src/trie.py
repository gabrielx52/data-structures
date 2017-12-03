"""Implement trie tree data structure."""


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize trie node."""
        self.structure = {}  # everything off root
        self.size = 0  # size of the tree

    def insert(self, string):
        """Insert input string into trie; ignore, if char already present."""

    def contains(self, string):
        """Return True if in string; False if not."""

    def size(self):
        """Return total number of words in trie; 0 if empty."""

    def remove(self, string):
        """Remove given string from trie; raise exception if not present."""
