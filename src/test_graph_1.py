"""Test graph data structure."""
import pytest


def test_init_isinstance_dict():
    """Test is g an instance of Graph."""
    from graph_1 import Graph
    g = Graph()
    assert isinstance(g, Graph)


def test_nodes_returns_list():
    """Test."""
    from graph_1 import Graph
    g = Graph()
    g_list = g.nodes()
    assert g_list == []


def test_add_edges_return_val():
    """."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(2, 3)
    assert g._g == {2: [3], 3: []}


def test_nodes_return_added_node_with_empty_list():
    """."""
    from graph_1 import Graph
    g = Graph()
    g.add_node(3)
    assert g._g[3] == []
