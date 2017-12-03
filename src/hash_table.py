"""Hash table data structure."""


class HashTable(object):
    """Hash table class."""

    def __init__(self, size=1024, hash_func='additive'):
        """Constructor method for hash table."""
        self.size = size
        self.hash_func = hash_func
        self.hash_table = [[] for i in range(size)]

    def get(self, key):
        """Get value from Hash table by key."""
        key_hash = self._hash(key)
        for i in self.hash_table[key_hash]:
            if i[0] == key:
                return i[1]

    def set(self, key, value):
        """Store value in hashed key bucket."""
        if isinstance(key, str):
            key_hash = self._hash(key)
            self.hash_table[key_hash].append([key, value])
        else:
            raise TypeError('Key must be a string.')

    def _hash(self, key):
        """Hashing method."""
        if self.hash_func == 'additive':
            return self._additive_hash(key)

    def _additive_hash(self, key):
        """Additive hash method."""
        hash_val = 0
        for i in key:
            hash_val += ord(i)
        return hash_val % self.size
