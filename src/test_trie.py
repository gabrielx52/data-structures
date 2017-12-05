"""Test trie implementation."""

import pytest


def test_init_trie_object():
    """Test initialization object."""
    from trie import Trie
    t = Trie()
    assert isinstance(t, Trie)


def test_init_trie_object_size():
    """Test initialization object, size."""
    from trie import Trie
    t = Trie()
    assert t.size == 0


def test_init_trie_object_():
    """Test initialization object."""
    from trie import Trie
    t = Trie()
    assert t.structure == {}


def test_insert_dict():
    """Test insert a string."""
    from trie import Trie, Node
    t = Trie()
    t.insert('apple')
    assert t.count == 5
