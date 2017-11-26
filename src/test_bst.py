"""Test binary search tree."""

import pytest


@pytest.fixture
def empty_tree():
    """Empty tree, i.e. no node."""
    from bst import BST
    bst = BST()
    return bst


@pytest.fixture
def blncd_tree():
    """Build balanced tree fixture."""
    from bst import BST
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
    return bst


@pytest.fixture
def unblncd_tree():
    """Build unbalanced tree fixture."""
    from bst import BST
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
    return bst


def test_init_isinstance_node(empty_tree):
    """Test node is node at initialization."""
    from bst import Node
    node = Node(50)
    assert isinstance(node, Node)


def test_bst_is_object():
    """Test object is an instance of object."""
    from bst import BST
    bst = BST()
    assert isinstance(bst, BST)


def test_insert_one_node(empty_tree):
    """Test insert inserts one node object."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    assert bst._size == 1


def test_insert_one_node_left_value_none(empty_tree):
    """Test insert inserts one node object."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    assert bst.root.left == None


def test_insert_two_nodes_one_lesser_so_left(empty_tree):
    """Test insert places lesser node to node root left."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    bst.insert(45)
    assert bst.root.left.val == 45


def test_insert_two_nodes_one_return_root(empty_tree):
    """Test insert places lesser node to node root left."""
    from bst import BST
    bst = BST()
    bst.insert(50)
    bst.insert(45)
    assert bst.root.val == 50
