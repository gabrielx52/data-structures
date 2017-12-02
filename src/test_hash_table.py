"""Test hash table."""

import pytest

def test Hashtable():
    """test is HashTable an instance."""
    from hash_table import HashTable
    h = HashTable(hash, 1)
    assert h is isinstance(HashTable)
