"""Tests for stack module."""


def test_stack_type():
    """Test stack instance type."""
    from stack import Stack
    stck = Stack()
    assert type(stck) == Stack
