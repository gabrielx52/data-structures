"""Test module for doubly linked list."""


def test_node_object():
    """Test new instance of node object."""
    from doubly_linked_list import Node
    assert type(Node()) == Node

