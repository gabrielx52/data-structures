"""Test module for Hash Table."""
import pytest


@pytest.fixture
def empty_hash_table():
    """Empty Hash Table fixture."""
    from hash_table import HashTable
    return HashTable()


@pytest.fixture
def empty_bern_hash():
    """Empty Hash Table fixture with Bern hash."""
    from hash_table import HashTable
    return HashTable(hash_func='bern')


@pytest.fixture
def full_hash_table():
    """Full Hash Table fixture."""
    from hash_table import HashTable
    ht = HashTable()
    with open('/usr/share/dict/words', 'r') as words:
        word_list = words.readlines()[:100]
    for word in word_list:
        ht.set(word.strip(), word.strip())
    return ht


def test_raise_value_error_with_bad_hash():
    """Test ValueError raised with bad hash."""
    from hash_table import HashTable
    with pytest.raises(ValueError):
        HashTable(hash_func='rat_hash')


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


def test_bern_hash_returns_correct_val(empty_bern_hash):
    """Test the bern hash returns hash of a single char."""
    assert empty_bern_hash._hash('a') == 206


def test_additive_hash_returns_correct_val_of_word(empty_hash_table):
    """Test the additive hash returns hash of string."""
    assert empty_hash_table._hash('abc') == 294


def test_bern_hash_returns_correct_val_of_word(empty_bern_hash):
    """Test the bern hash returns hash of string."""
    assert empty_bern_hash._hash('abc') == 339


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


def test_get_method_returns_value_in_hash_table_bern_hash(empty_bern_hash):
    """Test set method adds value to hash table."""
    empty_bern_hash.set('cat', 2)
    assert empty_bern_hash.get('cat') == 2


def test_get_method_on_full_hash_table(full_hash_table):
    """Test get method on hash table with collisions."""
    assert full_hash_table.get('Aaronic') == 'Aaronic'


def test_get_method_with_all_the_words(full_hash_table):
    """Test all the words are in the full hash table."""
    with open('/usr/share/dict/words', 'r') as words:
        word_list = words.readlines()[:100]
    for word in word_list:
        assert full_hash_table.get(word.strip()) == word.strip()


def test_add_duplicate_key_overwrite_previous_value(empty_hash_table):
    """Test when a key is inserted twice it will overwrite previous value."""
    empty_hash_table.set('cat', 1)
    empty_hash_table.set('cat', 'meow')
    assert empty_hash_table.get('cat') == 'meow'


def test_add_duplicate_key_overwrite_previous_value_bern_hash(empty_bern_hash):
    """Test when a key is inserted twice it will overwrite previous value."""
    empty_bern_hash.set('cat', 1)
    empty_bern_hash.set('cat', 'meow')
    assert empty_bern_hash.get('cat') == 'meow'
