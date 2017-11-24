"""Test module for BST."""
import types

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


def test_insert_one_node_on_empty_tree(empty_tree):
    """Test that inserted node on empty tree sets root to node."""
    empty_tree.insert(10)
    assert empty_tree._root.val == 10


def test_insert_node_with_string_as_value(empty_tree):
    """Test for TypeError when value is a string."""
    with pytest.raises(TypeError):
        empty_tree.insert('G')


def test_insert_method_inserts_nodes(empty_tree):
    """Test that insert method inserts nodes in correct order."""
    empty_tree.insert(10)
    empty_tree.insert(14)
    empty_tree.insert(16)
    empty_tree.insert(15)
    assert empty_tree._root.right.right.left.val == 15


def test_insert_duplicate_node_does_nothing(full_tree):
    """Test that inserting duplicate into tree doesn't insert it."""
    full_tree.insert(10)
    assert full_tree.size() == 8


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


def test_node_has_correct_children(full_tree):
    """Test that a node has the correct children."""
    node = full_tree.search(6)
    assert node.left.val == 4 and node.right.val == 8


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
    """Test that contains method returns False on empty tree."""
    assert empty_tree.contains(1) is False


def test_contains_returns_false_on_non_existent_node(full_tree):
    """Test that contains method returns False with non-existent node."""
    assert full_tree.contains(1) is False


def test_contains_returns_true_with_root_node(full_tree):
    """Test that contains method returns True with root node."""
    assert full_tree.contains(10) is True


def test_contains_returns_true_with_bottom_node(full_tree):
    """Test that contains method returns True with bottom node."""
    assert full_tree.contains(14) is True


def test_initiate_bst_with_list_of_numbers_iterable_works():
    """Test that BST obj takes iterable and creates a proper BST with it."""
    from bst import BST
    tree = BST([10, 12, 16, 6, 8, 4, 14, 2])
    assert tree.size() == 8


def test_initiate_bst_with_list_of_numbers_with_dupes():
    """Test that BST obj takes iterable with dupes and handles it properly."""
    from bst import BST
    tree = BST([10, 12, 16, 6, 6, 6, 8, 4, 14, 2, 6])
    assert tree.size() == 8


def test_initiate_bst_with_set_of_numbers_iterable_works():
    """Test that BST obj takes iterable and creates a proper BST with it."""
    from bst import BST
    tree = BST({10, 12, 16, 6, 8, 4, 14, 2})
    assert tree.size() == 8


def test_initiate_bst_with_int_raises_error():
    """Test that BST obj raises TypeError if given an int."""
    from bst import BST
    with pytest.raises(TypeError):
        BST('123445')


def test_initiate_bst_with_str_raises_error():
    """Test that BST obj raises TypeError if given a str."""
    from bst import BST
    with pytest.raises(TypeError):
        BST('string')


def test_in_order_method_returns_a_generator(full_tree):
    """Test the in-order method returns a generator."""
    in_order_gen = full_tree.in_order()
    assert isinstance(in_order_gen, types.GeneratorType)


def test_in_order_method_correctly_traverses_bst(full_tree):
    """Test the in-order method works correctly."""
    in_order_gen = full_tree.in_order()
    assert [n for n in in_order_gen] == [2, 4, 6, 8, 10, 12, 14, 16]


def test_in_order_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the in-order method returns a empty gen with empty tree."""
    in_order_gen = empty_tree.in_order()
    assert [n for n in in_order_gen] == []


def test_pre_order_method_returns_a_generator(full_tree):
    """Test the pre-order method returns a generator."""
    pre_order_gen = full_tree.pre_order()
    assert isinstance(pre_order_gen, types.GeneratorType)


def test_pre_order_method_correctly_traverses_bst(full_tree):
    """Test the pre-order method works correctly."""
    pre_order_gen = full_tree.pre_order()
    assert [n for n in pre_order_gen] == [10, 6, 4, 2, 8, 12, 16, 14]


def test_pre_order_method_returns_empty_gen_with_empty_tree(empty_tree):
    """Test the pre-order method returns a empty gen with empty tree."""
    pre_order_gen = empty_tree.pre_order()
    assert [n for n in pre_order_gen] == []
