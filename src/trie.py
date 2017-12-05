"""Trie Tree data structure."""


class TrieTree(object):
    """Trie Tree data structure class."""

    def __init__(self):
        """Constructor method."""
        self.root = {}
        self._size = 0

    def insert(self, string):
        """Insert string into Trie tree."""
        if not isinstance(string, str):
            raise TypeError('Input must be a string.')
        if self.contains(string):
            raise ValueError('Cannot insert duplicate words in tree.')
        else:
            self._size += 1
            current = self.root
            for letter in string:
                current = current.setdefault(letter, {})
            current['$'] = '$'

    def contains(self, string):
        """Return bool if string in Trie tree."""
        current = self.root
        for letter in string:
            if letter in current:
                current = current[letter]
            else:
                return False
        else:
            if '$' in current:
                return True
            return False

    def size(self):
        """Return size of Trie tree."""
        return self._size

    def remove(self, string):
        """Remove string from Trie tree."""
        if self.contains(string):
            self._size -= 1
            tmp = self.root
            tmp_str = list(string)
            for i in range(len(string)):
                for letter in tmp_str:
                    if tmp[letter] in ({'$': '$'}, {}):
                        del tmp[letter]
                        tmp_str.pop()
                    else:
                        tmp = tmp[letter]
                tmp = self.root
        else:
            raise ValueError('String not in tree.')
