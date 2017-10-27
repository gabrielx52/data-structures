"""Test module for doubly linked list."""


def test_node_object():
    """Test new instance of node object."""
    from doubly_linked_list import Node
    assert type(Node()) == Node


def test_dll_instance():
    """Test new instance of doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    assert type(DoublyLinkedList()) == DoublyLinkedList


def test_dll_push():
    """Test the push method on doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.push('one')
    dll.push('two')
    dll.push('three')
    assert dll._len == 3


def test_dll_append():
    """Test the append method on doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.append('one')
    dll.append('two')
    dll.append('three')
    assert dll._len == 3


def test_pop():
    """Test the pop method on doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.append('one')
    dll.append('two')
    dll.append('three')
    assert dll.pop() == 'one'

def test_shift():
    """Test the shift method on doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    dll = DoublyLinkedList()
    dll.append('one')
    dll.append('two')
    dll.append('three')
    assert dll.shift() == 'three'

