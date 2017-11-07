"""Test graph data structure."""
import pytest


def test_init_isinstance_dict():
    """."""
    from graph_1 import Graph
    g = Graph()
    assert isinstance(g, Graph)


def test_nodes_returns_list():
    """."""
    from graph_1 import Graph
    g = Graph()
    g_list = g.nodes()
    assert g_list == []



def test_nodes_return_added_node_with_empty_list():
    """."""
    from graph_1 import Graph
    g = Graph()
    g.add_node(3)
    assert g._g[3] == []

