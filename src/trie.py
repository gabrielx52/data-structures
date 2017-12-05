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
        return self._size

    def remove(self, string):
        """Remove string from Trie tree."""
        if self.contains(string):
            self._size -= 1
            tmp = self.root
            tmp_str = list(string)
            for i in range(len(string)):
                for l in tmp_str:
                    if tmp[l] == {'$': '$'} or tmp[l] == {}:
                        del tmp[l]
                        tmp_str.pop()
                    else:
                        tmp = tmp[l]
                tmp = self.root
        else:
            raise ValueError('String not in tree.')
