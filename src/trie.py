"""Trie Tree data structure."""


class TrieTree(object):
    """Trie Tree data structure class."""

    def __init__(self):
        """Constructor method."""
        self.root = {}

    def insert(self, string):
        """Insert string into Trie tree."""
        current = self.root
        for l in string:
            current = current.setdefault(l, {})
        current['$'] = '$'

    def contains(self, string):
        """Return bool if string in Trie tree."""
        current = self.root
        for l in string:
            if l in current:
                current = current[l]
            else:
                return False
        else:
            if '$' in current:
                return True
            else:
                return False

    def size(self):
        """Return size of Trie tree."""

    def remove(self, string):
        """Remove string from Trie tree."""
