"""Test trie implementation."""

import pytest
from trie import Node, Trie


def test_node_init_object():
    """Test initialization node object."""
    n = Node()
    assert isinstance(n, Node)


def test_node_init_children():
    """Test initialization object, children."""
    n = Node()
    assert n.children == {}


def test_node_init_terminus():
    """Test initialization node, terminus."""
    n = Node()
    assert n.terminus is False


def test_trie_init_parent():
    """Test size of Trie."""
    t = Trie()
    assert t.size == 0


def test_insert_dict():
    """Test insert a string."""
    t = Trie()
    t.insert('apple')
    assert 'a' in t.root.children

# t.root.children['a'] == 'a'