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


def test_insert_dict_key_where_expected():
    """Test insert holds proper key."""
    t = Trie()
    t.insert('apple')
    assert 'a' in t.root.children


def test_insert_dict_value_where_expected():
    """Test insert returns proper value."""
    t = Trie()
    t.insert('apple')
    assert isinstance(t.root.children['a'].children['p'], Node)


def test_contains_works():
    """Test contains works."""
    t = Trie()
    t.insert('apple')
    assert t.contains('apple') == True
