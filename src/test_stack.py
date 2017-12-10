"""Tests for stack module."""
import pytest


def test_stack_type():
    """Test stack instance type."""
    from stack import Stack
    stck = Stack()
    assert type(stck) == Stack


def test_push_and_pop():
    """Test the push and pop method on stack."""
    from stack import Stack
    stck = Stack()
    stck.push('one')
    stck.push('two')
    assert stck.pop() == 'two'


def test_stack_len():
    """Test the len function on stack."""
    from stack import Stack
    stck = Stack()
    stck.push('one')
    stck.push('two')
    assert len(stck) == 2


def test_pop_from_empty_stack_raises_error():
    """Test IndexError raised when pop from empty stack."""
    from stack import Stack
    stck = Stack()
    with pytest.raises(IndexError):
        stck.pop()
