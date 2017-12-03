"""Test module for Hash Table."""
import pytest


@pytest.fixture
def empty_hash_table():
    """Empty Hash Table fixture."""
    from hash_table import HashTable
    return HashTable()


@pytest.fixture
def full_hash_table():
    """Full Hash Table fixture."""
    from hash_table import HashTable
    ht = HashTable()
    with open('/usr/share/dict/words', 'r') as words:
        word_list = words.readlines()
    for word in word_list:
        ht.set(word.strip(), word.strip())
    return ht


def test_hash_table_is_hash_table_instance():
    """Test that hash table is HashTable type."""
    from hash_table import HashTable
    ht = HashTable()
    assert isinstance(ht, HashTable)


def test_hash_table_initial_length_is_1024(empty_hash_table):
    """Test hash table with no size arg has size of 1024."""
    assert empty_hash_table.size == 1024


def test_hash_table_with_size_arg_length_is_arg():
    """Test hash table with size arg has size of arg."""
    from hash_table import HashTable
    ht = HashTable(40)
    assert ht.size == 40


def test_additive_hash_returns_correct_val(empty_hash_table):
    """Test the additive hash returns ord value of a single char."""
    assert empty_hash_table._hash('a') == 97


def test_additive_hash_returns_correct_val_of_word(empty_hash_table):
    """Test the additive hash returns hash of string."""
    assert empty_hash_table._hash('abc') == 294


def test_set_method_sets_value_in_hash_table(empty_hash_table):
    """Test set method adds value to hash table."""
    empty_hash_table.set('cat', 2)
    assert [['cat', 2]] in empty_hash_table.hash_table


def test_set_method_raises_type_error_if_not_str(empty_hash_table):
    """Test that set method will raise a type error if key not str."""
    with pytest.raises(TypeError):
        empty_hash_table.set(1, 'cat')


def test_get_method_returns_value_in_hash_table(empty_hash_table):
    """Test set method adds value to hash table."""
    empty_hash_table.set('cat', 2)
    assert empty_hash_table.get('cat') == 2


def test_get_method_on_full_hash_table(full_hash_table):
    """Test get method on hash table with collisions."""
    assert full_hash_table.get('abed') == 'abed'


# def test_set_and_get_method_with_all_the_words(full_hash_table):
#     """Test all the words are in the full hash table."""
#     with open('/usr/share/dict/words', 'r') as words:
#         word_list = words.readlines()
#     for word in word_list:
#         assert full_hash_table.get(word.strip()) == word.strip()
