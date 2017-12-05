"""Test module for Trie Tree data structure."""
import pytest


@pytest.fixture
def empty_trie_tree():
    """Empty trie tree fixture."""
    from trie import TrieTree
    return TrieTree()


def test_trie_tree_is_trie_tree_instance():
    """Test that trie tree is an instance of trie tree."""
    from trie import TrieTree
    tt = TrieTree()
    assert isinstance(tt, TrieTree)


def test_insert_string_into_trie_tree(empty_trie_tree):
    """Test insert method trie tree."""
    empty_trie_tree.insert('test')
    assert 't' in empty_trie_tree.root.keys()


def test_insert_raises_type_error_if_not_string(empty_trie_tree):
    """Test insert raises TypeError if input is not a string."""
    with pytest.raises(TypeError):
        empty_trie_tree.insert(100)


def test_contains_method_with_trie_tree(empty_trie_tree):
    """Test contains method trie tree."""
    empty_trie_tree.insert('test')
    assert empty_trie_tree.contains('test')


def test_contains_method_returns_false_with_bad_word(empty_trie_tree):
    """Test contains method returns false bad word."""
    assert not empty_trie_tree.contains('test')


def test_contains_method_returns_false_with_close_match(empty_trie_tree):
    """Test contains method returns false with close word."""
    empty_trie_tree.insert('tests')
    assert not empty_trie_tree.contains('test')


def test_insert_duplicate_string_raises_error():
    """Test inserting duplicate string raises ValueError."""
    from trie import TrieTree
    tt = TrieTree()
    tt.insert('test')
    with pytest.raises(ValueError):
        tt.insert('test')


def test_size_method_on_empty_tree_returns_0(empty_trie_tree):
    """Test size method returns 0 on empty trie tree."""
    assert empty_trie_tree.size() == 0


def test_size_method_on_one_item_tree_returns_1(empty_trie_tree):
    """Test size method returns 1 on trie tree with one word."""
    empty_trie_tree.insert('Guido')
    assert empty_trie_tree.size() == 1


def test_remove_method_raise_error_if_bad_word(empty_trie_tree):
    """Test remove method raises error if word not in tree."""
    with pytest.raises(ValueError):
        assert not empty_trie_tree.remove('gabe')


def test_remove_method_on_single_item_trie_tree(empty_trie_tree):
    """Test remove method works on trie tree with one word."""
    empty_trie_tree.insert('gabe')
    empty_trie_tree.remove('gabe')
    assert not empty_trie_tree.contains('gabe')


def test_remove_method_on_trie_tree(empty_trie_tree):
    """Test remove method works on trie tree."""
    empty_trie_tree.insert('guido')
    empty_trie_tree.insert('gabe')
    empty_trie_tree.remove('gabe')
    assert not empty_trie_tree.contains('gabe')
    assert empty_trie_tree.contains('guido')


def test_size_correct_with_remove_method(empty_trie_tree):
    """Test size method reflects removed word."""
    empty_trie_tree.insert('guido')
    empty_trie_tree.insert('gabe')
    assert empty_trie_tree.size() == 2
    empty_trie_tree.remove('gabe')
    assert empty_trie_tree.size() == 1


def test_insert_delete_insert(empty_trie_tree):
    """Test insert and delete one item and insert new item."""
    empty_trie_tree.insert('guido')
    empty_trie_tree.remove('guido')
    empty_trie_tree.insert('gabe')
    assert empty_trie_tree.contains('gabe')
