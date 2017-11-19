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


@pytest.fixture
def trav_fixt():
    """Graph test fixture with nodes and edges."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(4, 7)
    g.add_edge(6, 8)
    g.add_edge(6, 9)
    g.add_edge(9, 10)
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


def test_add_edges_removes_duplicate_edge():
    """Test add edge adds an edge and removes old duplicate."""
    from graph_1 import Graph
    g = Graph()
    g.add_edge(2, 3)
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


def test_value_error_when_making_dup_node(g3_fixt):
    """Test a ValueError gets raised if attempting to make a duplicate node."""
    with pytest.raises(ValueError):
        g3_fixt.add_node(1)


def test_value_error_with_self_referrencing_edge(g3_fixt):
    """Test a ValueError gets raised if attempting to make a duplicate node."""
    with pytest.raises(ValueError):
        g3_fixt.add_edge(1, 1)


def test_del_node_also_deletes_edges_to_deleted_node(g3_fixt):
    """Test that edges to deleted node are also deleted."""
    g3_fixt.add_edge(2, 1)
    g3_fixt.del_node(1)
    assert g3_fixt.edges() == []


def test_neighbors_returns_list_of_neighbor_nodes(g3_fixt):
    """Test that neighbors method returns list of neighbor nodes."""
    g3_fixt.add_edge(1, 2)
    g3_fixt.add_edge(1, 3)
    g3_fixt.add_edge(1, 4)
    assert g3_fixt.neighbors(1) == [2, 3, 4]


def test_neighbors_of_non_existent_node_returns_value_error(g3_fixt):
    """Test that neighbors method raises error if node isn't in graph."""
    with pytest.raises(ValueError):
        g3_fixt.neighbors(4)


def test_adjacent_method_returns_false_on_non_adjacent_nodes(g3_fixt):
    """Test that adjacent method returns false if nodes are not adjacent."""
    assert g3_fixt.adjacent(1, 2) is False


def test_adjacent_method_returns_true_on_adjacent_nodes(g3_fixt):
    """Test that adjacent method returns true if nodes are adjacent."""
    g3_fixt.add_edge(1, 2)
    assert g3_fixt.adjacent(1, 2) is True


def test_adjacent_method_raises_error_if_firstt_node_not_in_graph(g3_fixt):
    """Test that adjacent method raise error if first node is not in graph."""
    with pytest.raises(ValueError):
        g3_fixt.adjacent(5, 1)


def test_adjacent_method_raises_error_if_second_node_not_in_graph(g3_fixt):
    """Test that adjacent method raise error if second node is not in graph."""
    with pytest.raises(ValueError):
        g3_fixt.adjacent(1, 5)


def test_adjacent_method_raises_error_if_both_nodes_not_in_graph(g3_fixt):
    """Test that adjacent method raise error if both nodes are not in graph."""
    with pytest.raises(ValueError):
        g3_fixt.adjacent(4, 5)


def test_breadth_first_traversal(trav_fixt):
    """Test breadth first traversal properly traverses graph."""
    assert trav_fixt.breadth_first_traversal(1) == [1, 2, 3,
                                                    4, 5, 6, 7,
                                                    8, 9, 10]


def test_breadth_first_traversal_multi_pointers(trav_fixt):
    """Test breadth first traversal with multi pointers to same node."""
    trav_fixt.add_edge(2, 7)
    assert trav_fixt.breadth_first_traversal(1) == [1, 2, 3,
                                                    4, 5, 6, 7,
                                                    8, 9, 10]


def test_breadth_first_traversal_cycle(trav_fixt):
    """Test breadth first traversal properly traverses graph with cycle."""
    trav_fixt.add_edge(10, 1)
    assert trav_fixt.breadth_first_traversal(1) == [1, 2, 3,
                                                    4, 5, 6, 7,
                                                    8, 9, 10]
