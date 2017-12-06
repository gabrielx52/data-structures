"""Implement trie tree data structure."""

import pdb


class Node(object):
    """Create node object."""

    def __init__(self):
        """Node object on initialization."""
        self.children = None
        self.parent = None
        self.terminus = False


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie tree."""
        self.size = 0
        self.root = Node(None)

    def insert(self, word):
        """Insert input string into trie; ignore, if char already present."""
        current = self.root
        count = 0
        for letter in range(word):
            if letter not in current.children:
                new = Node(letter)
                new.parent = current
                current.children[letter] = new
                current = new
                count += 1
        current.terminus = True
        self.size += 1

    def contains(self, string):
        """Return True if in string; False if not."""
        try:
            return self[string]
        except KeyError:
            print('The word is not in your trie tree')

    def size(self):
        """Return total number of words in trie; 0 if empty."""
        return self.count

    def remove(self, string):
        """Remove given string from trie; raise exception if not present."""
        pass
