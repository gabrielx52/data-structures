"""Test module for linked list module."""


def test_linked_list_instance():
    """Test new instance of LinkedList obj."""
    from linked_list import LinkedList
    assert type(LinkedList()) == LinkedList


def test_node_instance():
    """Test new instance of Node obj."""
    from linked_list import Node
    assert type(Node()) == Node


def test_pop():
    """Test linked list pop method."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('val')
    assert ll.pop() == 'val'


def test_linked_list_count():
    """Test linked list object count."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.push('three')
    assert ll.count == 3


def test_linked_list_size():
    """Test linked list size method."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.pop()
    assert ll.size() == 1
