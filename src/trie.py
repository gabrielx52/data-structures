"""Implement trie tree data structure."""

import pdb


class Node(object):
    """Create node object."""
    def __init___(self, character, parent):
        """Node object on initialization."""
        self.character = character
        self.parent = parent
        self.terminus = False

class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie tree."""
        self.root = Node(None, None)
        self.structure = {}  # everything off root
        self.size = 0

    def insert(self, word):
        """Insert input string into trie; ignore, if char already present."""
        if not word:
            return
        current_node = self.root


        if head in self.structure:
            head

    def contains(self, string):
        """Return True if in string; False if not."""
        try:
            return self[string]
        except KeyError:
            print('The word is not in your trie tree')

    def size(self):
        """Return total number of words in trie; 0 if empty."""

    def remove(self, string):
        """Remove given string from trie; raise exception if not present."""
