"""Implement two hash tables, one additive and another of choice.\

Examples found in http://www.partow.net/programming/hashfunctions/\

https://www.quora.com/How-do-I-create-my-own-hash-table-implementation-in-Python\"""

table = [[] for x in range(10)]

class HashTable:
    """Build HashTable class."""
    def __init__(self):
      self.table = table

    def



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

"""initialize a table of zeros."""
