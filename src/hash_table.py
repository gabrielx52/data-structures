"""Implement two hash tables, one additive and another of choice.\

Examples found in http://www.partow.net/programming/hashfunctions/\

www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python."""

def naive_hash(value):
    """Simple hash function."""
    if value is not str:
        raise TypeError("Need to pass a word into the hash, i.e. a string")
    hash_val = 0
    for letter in value:
        hash_val += ord(letter)
    return hash_val % self.size


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
        hash_bucket = self._hash(key)
        for bucket in range(len(hash_bucket)):
            if hash_bucket[bucket][0] == key:
                hash_bucket[bucket] = (key, value)
        hash_bucket.append((key, value))



    def get(self, key):
        """Return value stored in the given key."""

    def _hash(self, key):
        """Hash the key provided."""
        return hash(key)

    def set(self, key, data):
        """Insert value in table."""
        # table[DJBHash(input)].append(data)
        # import pdb; pdb.set_trace()
        hashvalue = self.hash(key, len(self.buckets))

        if self.buckets[hashvalue] is None:
            self.buckets[hashvalue] == key
            self.data == data

        else:
            if self.buckets[hashvalue] == key:
                self.data[hashvalue] == data
            else:
                nextbucket = self.rehash(hashvalue, len(self.buckets))
                while self.buckets[nextbucket] is not None and \
                        self.buckets[nextbucket] != key:
                    nextbucket = self.rehash(nextbucket, len(self.buckets))

                if self.buckets[nextbucket] is None:
                    self.buckets[nextbucket] = key
                    self.buckets[nextbucket] = data

                else:
                    self.data[nextbucket] = data

    def get_key(self, key):
        """."""
        startbucket = self.hash(key, len(self.buckets))
        data = None
        stop = False
        found = False
        position = startbucket
        while self.buckets[position] is not None and \
                not found and not stop:
            if self.buckets[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.buckets))
                if position == startbucket:
                    stop = True
        return data

    def get_item(self, key):
        """."""
        return self.get(key)

    def set_item(self, key, data):
        """."""
        return self.set(key, data)

    def hash(self, key, size):
        """."""
        return key % size

    def rehash(self, oldhash, size):
        """."""
        return (oldhash + 1) % size

    def simple_hash(self, value):
        str_val = split(value, "")


    def DJBHash(key):  # pragma no cover
        """Additive Hash produced by D.J. Bernstein originally pub usenet newsgroup."""
        hash = 5381
        for i in range(len(key)):
            hash = ((hash << 5) + hash) + ord(key[i])
        return hash


    def ELFHash(key):  # pragma no cover
        """Hash function, widely used in unix based systems, 32 bit processors."""
        hash = 0
        x    = 0
        for i in range(len(key)):
          hash = (hash << 4) + ord(key[i])
          x = hash & 0xF0000000
          if x != 0:
            hash ^= (x >> 24)
          hash &= ~x
        return hash
