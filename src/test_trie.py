"""Test trie implementation."""

import pytest


def test_node_init_object():
    """Test initialization object."""
    from trie import Node
    n = Node()
    assert isinstance(n, Node)


def test_node_init_children():
    """Test initialization object, size."""
    from trie import Node
    n = Node()
    assert n.children is None


def test_node_init_terminus():
    """Test initialization object."""
    from trie import Node
    n = Node()
    assert n.terminus is False


# def test_insert_dict():
#     """Test insert a string."""
#     from trie import Trie, Node
#     t = Trie()
#     t.insert('apple')
#     assert t.count == 5
