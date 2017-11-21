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


def test_bst_depth_attr_empty_tree(empty_tree):
    """Test depth attr is 0 with empty tree."""
    assert empty_tree._depth == 0


def test_bst_depth_attr_full_tree(full_tree):
    """Test depth attr is correct depth of tree with nodes."""
    assert full_tree._depth == 3


def test_bst_depth_method_empty_tree(empty_tree):
    """Test depth method returns 0 with empty tree."""
    assert empty_tree.depth() == 0


def test_bst_depth_method_full_tree(full_tree):
    """Test depth method returns correct depth of tree with nodes."""
    assert full_tree.depth() == 3


def test_bst_balance_method_on_empty_tree(empty_tree):
    """"Test balance method returns 0 on empty tree."""
    assert empty_tree.balance() == 0


def test_bst_balance_attr_on_empty_tree(empty_tree):
    """"Test balance attr is 0 on empty tree."""
    assert empty_tree._balance == 0


def test_bst_balance_method_on_left_balanced_tree(full_tree):
    """"Test balance method returns 1 on left balanced tree."""
    assert full_tree.balance() == 1


def test_bst_balance_attr_on_left_balanced_tree(full_tree):
    """"Test balance attr is 1 on left balanced tree."""
    assert full_tree._balance == 1


def test_bst_balance_method_on_balanced_tree(full_tree):
    """"Test balance method returns 0 on balanced tree."""
    full_tree.insert(18)
    assert full_tree.balance() == 0


def test_bst_balance_attr_on_balanced_tree(full_tree):
    """"Test balance attr is 0 on balanced tree."""
    full_tree.insert(18)
    assert full_tree._balance == 0


def test_bst_balance_method_on_right_balanced_tree(full_tree):
    """"Test balance method returns -1 on right balanced tree."""
    full_tree.insert(18)
    full_tree.insert(20)
    assert full_tree.balance() == -1


def test_bst_balance_attr_on_right_balanced_tree(full_tree):
    """"Test balance attr is -1 on right balanced tree."""
    full_tree.insert(20)
    full_tree.insert(18)
    assert full_tree._balance == -1


def test_bst_balance_method_on_really_right_balanced_tree(empty_tree):
    """Test balance method returns correct balance on really right tree."""
    for i in range(1, 21):
        empty_tree.insert(i)
    assert empty_tree.balance() == -19


def test_bst_balance_method_on_really_left_balanced_tree(empty_tree):
    """Test balance method returns correct balance on really left tree."""
    for i in range(21, 1, -1):
        empty_tree.insert(i)
    assert empty_tree.balance() == 19


def test_search_returns_none_on_empty_tree(empty_tree):
    """Test that search method returns None on empty tree."""
    assert empty_tree.search(1) is None


def test_search_returns_none_on_non_existent_node(full_tree):
    """Test that search method returns None with non-existent node."""
    assert full_tree.search(99) is None


def test_search_returns_node_obj_when_found(full_tree):
    """Test that search method returns Node object when node is found."""
    from bst import Node
    assert isinstance(full_tree.search(10), Node)


def test_search_returns_node_with_correct_value_when_found(full_tree):
    """Test that search method returns Node with correct value when found."""
    assert full_tree.search(10).val == 10


def test_search_returns_node_at_bottom_of_tree(full_tree):
    """Test that search method returns Node at bottom of the tree."""
    assert full_tree.search(16).val == 16


def test_contains_returns_false_on_empty_tree(empty_tree):
    """Test that contains method returns false on empty tree."""
    assert empty_tree.contains(1) is False


def test_contains_returns_false_on_non_existent_node(full_tree):
    """Test that contains method returns false with non-existent node."""
    assert full_tree.contains(1) is False
