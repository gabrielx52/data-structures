"""Test module for BST."""
import pytest


@pytest.fixture
def empty_tree():
    """Empty BST fixture."""
    from bst import BST
    tree = BST()
    return tree


@pytest.fixture
def full_tree():
    """Full BST fixture."""
    from bst import BST
    tree = BST()
    tree.insert(10)
    tree.insert(12)
    tree.insert(16)
    tree.insert(6)
    tree.insert(8)
    tree.insert(4)
    tree.insert(14)
    tree.insert(2)
    return tree


def test_node_is_node_class():
    """Test that node is an instance of Node."""
    from bst import Node
    n = Node(1)
    assert isinstance(n, Node)


def test_bst_is_bst_object():
    """Test that bst is an instance of BST."""
    from bst import BST
    tree = BST()
    assert isinstance(tree, BST)


def test_bst_size_attr_empty_tree(empty_tree):
    """Test size attr is 0 with empty tree."""
    assert empty_tree._size == 0


def test_bst_size_attr_full_tree(full_tree):
    """Test size attr is correct size of tree with nodes."""
    assert full_tree._size == 8


def test_bst_size_method_empty_tree(empty_tree):
    """Test size method returns 0 with empty tree."""
    assert empty_tree.size() == 0


def test_bst_size_method_full_tree(full_tree):
    """Test size method returns correct size of tree with nodes."""
    assert full_tree.size() == 8
