"""Test module for Trie Tree data structure."""


def test_trie_tree_is_trie_tree_instance():
    """Test that trie tree is an instance of trie tree."""
    from trie import TrieTree
    tt = TrieTree()
    assert isinstance(tt, TrieTree)


def test_insert_string_into_trie_tree():
    """Test insert method trie tree."""
    from trie import TrieTree
    tt = TrieTree()
    tt.insert('test')
    assert 't' in tt.root.keys()


def test_contains_method_with_trie_tree():
    """Test contains method trie tree."""
    from trie import TrieTree
    tt = TrieTree()
    tt.insert('test')
    assert tt.contains('test')
