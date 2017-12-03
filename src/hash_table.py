"""Implement two hash tables, one additive and another of choice.\

Examples found in http://www.partow.net/programming/hashfunctions/\

www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python."""

import pdb


def naive_hash(value, size):
        """Simple hash function."""
        if not isinstance(value, str):
            raise TypeError("Need to pass a word into the hash, i.e. a string")
        hash_val = 0
        for letter in value:
            hash_val += ord(letter)
        return hash_val % size


class HashTable(object):
    """Build HashTable class."""

    def __init__(self, size, hash_func=naive_hash):
        """."""
        self.buckets = []
        self.size = size
        self.hash_func = hash_func
        for bucket in range(self.size):
            self.buckets.append([])

    def set(self, key, value):
        """Store given value using given key."""
        hash_key = self._hash(key)
        if self.buckets[hash_key] == []:
            self.buckets[hash_key].append((key, value))

        # for item in range(len(self.buckets[hash_key]):
        #     if self.buckets[hash_key][item][0] == key:

        #         item = (key, value)
        # self.buckets[hash_key].append((key, value))

    # def get(self, key):
    #     """Return value stored in the given key."""
    #     hash_bucket = self._hash(key)
    #     for word_string in hash_bucket:
    #         if word_string[0] == key[1]:
    #             return key
    #     return None

    def _hash(self, key):
        """Hash the key provided."""
        return self.hash_func(key, self.size)


    # def DJBHash(key):  # pragma no cover
    #     """Additive Hash produced by D.J. Bernstein originally pub usenet newsgroup."""
    #     hash = 5381
    #     for i in range(len(key)):
    #         hash = ((hash << 5) + hash) + ord(key[i])
    #     return hash


    # def ELFHash(key):  # pragma no cover
    #     """Hash function, widely used in unix based systems, 32 bit processors."""
    #     hash = 0
    #     x    = 0
    #     for i in range(len(key)):
    #       hash = (hash << 4) + ord(key[i])
    #       x = hash & 0xF0000000
    #       if x != 0:
    #         hash ^= (x >> 24)
    #       hash &= ~x
    #     return hash
