"""Implement two hash tables, one additive and another of choice.\

Examples found in http://www.partow.net/programming/hashfunctions/\

https://www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python\"""

foo = [[] for x in range(1024)]

class HashTable:
    """Build HashTable class."""
    def __init__(self, size, buckets, data):
      self.size = size
      self.buckets = [None] * self.size
      self.data = [None] * self.size



    def set(self, key, data):
      """Insert value in table."""
      # table[DJBHash(input)].append(data)
      hashvalue = self.hashfunction(key, len(self.buckets))

      if self.buckets[hashvalue] == None:
        self.buckets[hashvalue] == key
        self.data == data

      else:
        if self.buckets[hashvalue] == key:
          self.data[hashvalue] == data
        else:
          nextbucket = self.rehash(hashvalue, len(self.buckets))
          while self.buckets[nextbucket] != None and \
            self.buckets[nextbucket] != key:
            nextbucket = self.rehash(nextbucket, len(self.buckets))

          if self.buckets[nextbucket] = None:
            self.buckets[nextbucket] = key
            self.buckets[nextbucket] = data

          else:
            self.data[nextbucket] = data


    def get_key(self, key):
      """."""
      startbucket = self.hashfunction(key, len(self.buckets))
      data = None
      stop = False
      found = False
      position = startbucket
      while self.buckets[position] != None and \
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
        return self.get(key)

      def set_item(self, key, data):
        return self.set(key, data)

      def hash(self, key, size):
        return key%size

      def rehash(self, oldhash, size):
        return (oldhash+1)%size


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
