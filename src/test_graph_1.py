"""Test graph data structure."""
import pytest


@pytest.fixture
def g3_fixt():
    """Graph test fixture with 3 nodes."""
    from graph_1 import Graph
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    return g


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
    """Test add edge adds an edge to val1 node."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(2, 3)
    assert g._g == {2: [3], 3: []}


def test_nodes_return_added_node_with_empty_list():
    """Test add node creates empty dict as starting value."""
    from graph_1 import Graph
    g = Graph()
    g.add_node(3)
    assert g._g[3] == []


def test_edges_method_returns_list_of_tuples_of_edges(g3_fixt):
    """Test that edges method returns list of edge tuples."""
    g3_fixt.add_edge(1, 2)
    g3_fixt.add_edge(1, 3)
    g3_fixt.add_edge(2, 3)
    assert g3_fixt.edges() == [(1, 2), (1, 3), (2, 3)]


def test_del_node_removes_node(g3_fixt):
    """Test node removed."""
    g3_fixt.del_node(1)
    assert g3_fixt.nodes() == [2, 3]


def test_del_node_raises_error_if_not_value(g3_fixt):
    """Test graph raises error if no node detected."""
    with pytest.raises(ValueError):
        g3_fixt.del_node(4)


def test_del_edge_deletes_an_edge(g3_fixt):
    """Test that del_edge method deletes an edge."""
    g3_fixt.add_edge(1, 2)
    g3_fixt.del_edge(1, 2)
    assert g3_fixt.edges() == []


def test_del_edge_raises_error_for_non_existent_node(g3_fixt):
    """Test that del_edge raises value error when passed non-existent node."""
    with pytest.raises(ValueError):
        g3_fixt.del_edge(1, 4)


def test_del_edge_raises_error_for_non_existent_edge(g3_fixt):
    """Test that del_edge raises value error when passed non-existent edge."""
    with pytest.raises(ValueError):
        g3_fixt.del_edge(1, 3)


def test_has_node_return_true_if_node_present(g3_fixt):
    """Test has_node method returns True if node exists."""
    assert g3_fixt.has_node(1) is True


def test_has_node_return_false_if_node_not_present(g3_fixt):
    """Test has_node method returns False if node doesn't exist."""
    assert g3_fixt.has_node(4) is False
