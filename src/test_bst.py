"""Test binary search tree."""

import pytest

@pytest.fixture
def empty_tree():
"""Empty tree, i.e. no node."""
    return BST()

@pytest.fixture
def blncd_tree():
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(15)
bst.insert(25)
bst.insert(35)
bst.insert(45)
bst.insert(70)
bst.insert(60)
bst.insert(90)
bst.insert(55)
bst.insert(65)
bst.insert(80)
bst.insert(100)


@pytest.fixture
def unblncd_tree():
bst = BST()
bst.insert(50)
bst.insert(40)
bst.insert(30)
bst.insert(45)
bst.insert(25)
bst.insert(35)
bst.insert(43)
bst.insert(48)
bst.insert(60)
bst.insert(70)
bst.insert(80)

def test_node_isinstance_node():
    """Test node is node at initialization."""
    from bst import Node
    node = Node()
    node isinstance(node, Node)
