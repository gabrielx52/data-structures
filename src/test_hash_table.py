"""Test hash table."""

import pytest


def test_hash_table():
    """test is HashTable an instance."""
    from hash_table import HashTable
    h = HashTable(11, 1)
    assert isinstance(h, HashTable)
