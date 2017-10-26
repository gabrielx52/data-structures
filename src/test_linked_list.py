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
    assert ll._count == 3


def test_linked_list_size():
    """Test linked list size method."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.pop()
    assert ll.size() == 1


def test_linked_list_search():
    """Test linked list search method."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('val')
    ll.push('val2')
    ll.push('val3')
    assert ll.search('val3').data == 'val3'


def test_len_function_linked_list():
    """Test len function with linked list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.pop()
    assert len(ll) == 1


def test_linked_list_remove():
    """Test remove method of linked list."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.push('three')
    node = ll.search('two')
    ll.remove(node)
    assert len(ll) == 2


def test_linked_list_display():
    """Test display the linked list as if a tuple literal."""
    from linked_list import LinkedList
    ll = LinkedList()
    ll.push('one')
    ll.push('two')
    ll.push('three')
    assert ll.display() == "('one', 'two', 'three')"


def test_linked_list_iterable():
    """Test LinkedList iterable loader."""
    from linked_list import LinkedList
    ll = LinkedList(['one', 'two', 'three'])
    assert ll.head.data == 'three'
