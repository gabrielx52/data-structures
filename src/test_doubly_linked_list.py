"""Test module for doubly linked list."""
import pytest


@pytest.fixture
def dll_fixture():
    """Set up test fixture for doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    return DoublyLinkedList()


def test_node_object():
    """Test new instance of node object."""
    from doubly_linked_list import Node
    assert type(Node(None, None, None)) == Node


def test_dll_instance():
    """Test new instance of doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    assert type(DoublyLinkedList()) == DoublyLinkedList


def test_dll_push(dll_fixture):
    """Test the push method on doubly linked list."""
    dll_fixture.push('one')
    dll_fixture.push('two')
    dll_fixture.push('three')
    assert dll_fixture._len == 3


def test_dll_append(dll_fixture):
    """Test the append method on doubly linked list."""
    dll_fixture.append('one')
    dll_fixture.append('two')
    dll_fixture.append('three')
    dll_fixture.push('zero')
    assert dll_fixture._len == 4


def test_single_node_head_equals_tail(dll_fixture):
    """Test that head equals tail in single node dll."""
    dll_fixture.push('one')
    assert dll_fixture.head == dll_fixture.tail


def test_pop(dll_fixture):
    """Test the pop method on doubly linked list."""
    dll_fixture.push('one')
    dll_fixture.push('two')
    dll_fixture.push('three')
    assert dll_fixture.pop() == 'three'


def test_pop_dll_of_one(dll_fixture):
    """Test the pop method on doubly linked list of len one."""
    dll_fixture.append('one')
    assert dll_fixture.pop() == 'one'


def test_shift(dll_fixture):
    """Test the shift method on doubly linked list."""
    dll_fixture.append('one')
    dll_fixture.append('two')
    dll_fixture.append('three')
    assert dll_fixture.shift() == 'three'


def test_shift_dll_of_one(dll_fixture):
    """Test the shift method on doubly linked list of len one."""
    dll_fixture.append('one')
    assert dll_fixture.shift() == 'one'


def test_len_dll(dll_fixture):
    """Test len function on doubly linked list."""
    dll_fixture.append('one')
    dll_fixture.push('two')
    dll_fixture.push('three')
    assert len(dll_fixture) == 3


def test_dll_remove(dll_fixture):
    """Test remove method on doubly linked list."""
    dll_fixture.append('one')
    dll_fixture.push('two')
    dll_fixture.append('three')
    dll_fixture.remove('two')
    assert len(dll_fixture) == 2


def test_dll_remove_value_error(dll_fixture):
    """Test dll remove method error handling ."""
    dll_fixture.append('one')
    dll_fixture.append('two')
    dll_fixture.append('three')
    with pytest.raises(ValueError):
        dll_fixture.remove('to')


def test_int_push_and_remove(dll_fixture):
    """Test doubly linked list push and remove with ints."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(3)
    dll_fixture.remove(2)
    assert len(dll_fixture) == 2


def test_remove_first_instance(dll_fixture):
    """Test remove method with multiple nodes with same value."""
    dll_fixture.push(1)
    dll_fixture.push(2)
    dll_fixture.push(2)
    dll_fixture.remove(2)
    assert len(dll_fixture) == 2


def test_remove_only_instance(dll_fixture):
    """Test remove method with one node in dll."""
    dll_fixture.push(1)
    dll_fixture.remove(1)
    assert len(dll_fixture) == 0


def test_remove_tail_node(dll_fixture):
    """Test remove method with tail node."""
    dll_fixture.push(1)
    dll_fixture.push('two')
    dll_fixture.push('3')
    dll_fixture.remove(1)
    assert len(dll_fixture) == 2


def test_remove_head_node(dll_fixture):
    """Test remove method with head node."""
    dll_fixture.push(1)
    dll_fixture.push('two')
    dll_fixture.push('3')
    dll_fixture.remove('3')
    assert len(dll_fixture) == 2
