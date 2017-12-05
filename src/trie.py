"""Implement trie tree data structure."""

import pdb


class Node(object):
    """Create node object."""
    def __init___(self, parent):
        """Node object on initialization."""
        self.children = [None] * 26
        self.parent = parent
        self.terminus = False


class Trie(object):
    """Trie class."""

    def __init__(self):
        """Initialize the trie tree."""
        self.nodes = {}  # word off root
        self.size = 0

    def insert(self, word):
        """Insert input string into trie; ignore, if char already present."""
        root = Node(None)
        for char in range(word):
            current_node = Node(char)
            if current_node not in current_node.children
                self.nodes[current_node] = current_node.children

            elif current_node is root.child:
                self.nodes[current_node.child]

            if current_node is root.child:
                current_node = ()


        current_node = Node(word)
            while current_node[0]:
                if current_node[0] is not self.root.child:
                    current_node[0] = self.child
                    for letter in range(current_node[1:]):
                        self.nodes[letter] =




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
