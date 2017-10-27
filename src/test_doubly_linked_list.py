"""Test module for doubly linked list."""


def test_node_object():
    """Test new instance of node object."""
    from doubly_linked_list import Node
    assert type(Node()) == Node


def test_dll_instance():
    """Test new instance of doubly linked list."""
    from doubly_linked_list import DoublyLinkedList
    assert type(DoublyLinkedList()) == DoublyLinkedList
