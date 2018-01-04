"""Implement two hash tables, one additive and another of choice.\

Examples found in http://www.partow.net/programming/hashfunctions/\

www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python."""


class HashTable(object):
    """Build HashTable class."""

    def __init__(self, size, hash_func='naive_hash'):
        """Initialize hashTable."""
        self.buckets = []
        self.size = size
        self.hash_func = hash_func
        for bucket in range(self.size):
            self.buckets.append([])

    def djb_hash(self, value):  # pragma no cover
            """Hash produced by D.J. Bernstein originally pub usenet newsgroup."""
            hash = 5381
            for i in range(len(value)):
                hash = ((hash << 5) + hash) + ord(value[i])
            return hash % self.size

    def naive_hash(self, value):
            """Simple hash function."""
            if not isinstance(value, str):
                raise TypeError("Need to pass a word into the hash, i.e. a string")
            hash_val = 0
            for letter in value:
                hash_val += ord(letter)
            return hash_val % self.size

    def set(self, key, value):
        """Store given value using given key."""
        hash_key = self._hash(key)
        if self.buckets[hash_key] == []:
            self.buckets[hash_key].append((key, value))
        else:
            for item in range(len(self.buckets[hash_key])):
                if self.buckets[hash_key][item][0] == key:
                    self.buckets[hash_key][item] = (key, value)
                else:
                    self.buckets[hash_key].append((key, value))

    def get(self, key):
        """Return value stored in the given key."""
        hash_bucket = self._hash(key)
        if self.buckets[hash_bucket]:
            for item in self.buckets[hash_bucket]:
                if item[0] == key:
                    return item[1]
        else:
            return None

    def _hash(self, key):
        """Hash the key provided."""
        if self.hash_func == 'naive_hash':
            return self.naive_hash(key)
        if self.hash_func == 'djb_hash':
            return self.djb_hash(key)
