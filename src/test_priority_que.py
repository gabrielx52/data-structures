"""Test for test_priority que."""
import pytest

def test_priority_que():
    from priority_que import PriorityQ
    pq = PriorityQ()
    assert isinstance(pq, PriorityQ)
