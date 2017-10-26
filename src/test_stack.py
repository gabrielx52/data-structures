"""Tests for stack module."""


def test_stack_type():
    """Test stack instance type."""
    from stack import Stack
    stck = Stack()
    assert type(stck) == Stack

def test_push_and_pop():
    """Test the push and pop method of stack."""
    from stack import Stack
    stck = Stack()
    stck.push('one')
    stck.push('two')
    assert stck.pop() == 'two'
