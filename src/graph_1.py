"""Graph data structure."""


class Graph(object):
    """Graph data structure class."""

    def __init__(self):
        """Constructor method for graph."""
        self._g = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self._g.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        vals = list(self._q.values())
        edges = [item for sublist in vals for item in sublist]
        return edges

    def add_node(self, val):
        """Add a new node to the graph."""
        if val in self._g.keys():
            raise ValueError('Node already exists.')
        self._g[val] = []

    def add_edge(self, val1, val2):
        """Add a new edge to the graph."""
        if val1 not in self.nodes():
            self.add_node(val1)
        if val2 not in self.nodes():
            self.add_node(val2)
        if val2 == val1:
            raise ValueError('Cannot have a self-referential edge.')
        tmp = self._g[val1]
        tmp.append(val2)
        self._g[val1] = list(set(tmp))

    def del_node(self, val):
        """Delete the node containing ‘val’."""

    def del_edge(self, val1, val2):
        """Delete an edge from the graph."""

    def has_node(self, val):
        """True if node present in graph, else False."""

    def neighbors(self, val):
        """Return the list of all node's neighbor nodes."""

    def adjacent(self, val1, val2):
        """True if edge connecting val1 and val2, else False."""
