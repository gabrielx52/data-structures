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
        edges = []
        for key in self._g:
            if self._g[key]:
                for value in self._g[key]:
                    edges.append((key, value, self._g[key][value]))
        return edges

    def add_node(self, val):
        """Add a new node to the graph."""
        if val in self._g:
            raise ValueError('Node already exists.')
        self._g[val] = {}

    def add_edge(self, val1, val2, weight=0):
        """Add a new edge to the graph."""
        if val1 not in self._g:
            self.add_node(val1)
        if val2 not in self._g:
            self.add_node(val2)
        if val2 == val1:
            raise ValueError('Cannot have a self-referential edge.')
        if val2 in self._g[val1]:
            del self._g[val1][val2]
        self._g[val1][val2] = weight

    def del_node(self, val):
        """Delete the node containing ‘val’."""
        if val in self._g:
            for node in self._g:
                if val in self._g[node]:
                    del self._g[node][val]
            del self._g[val]
        else:
            raise ValueError('{} not in graph'.format(val))

    def del_edge(self, val1, val2):
        """Delete an edge from the graph."""
        if val1 in self._g and val2 in self._g:
            if val2 in self._g[val1]:
                del self._g[val1][val2]
            else:
                raise ValueError('Cannot remove non_existent edge.')
        else:
            raise ValueError('Cannot remove non-existent edge.')

    def has_node(self, val):
        """True if node present in graph, else False."""
        return val in self._g

    def neighbors(self, val):
        """Return the list of all node's neighbor nodes."""
        if val in self._g:
            return list(self._g[val].keys())
        else:
            raise ValueError('Node not in graph')

    def adjacent(self, val1, val2):
        """True if edge connecting val1 and val2, else False."""
        if val1 in self._g and val2 in self._g:
            return val2 in self._g[val1]
        raise ValueError('Nodes must be in graph')

    def breadth_first_traversal(self, start_val):
        """Return visited path of breadth first traversal."""
        traversed = []
        visited, queue = set(), []
        queue.append(start_val)
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            queue.extend(self._g[current])
            traversed.append(current)
        return traversed

    def depth_first_traversal(self, start_val):
        """Traverse a stack."""
        set_traversed = []
        visited = set()
        stack = []
        stack.append(start_val)
        while stack:
            visited_node = stack.pop()
            if visited_node in visited:
                continue
            visited.add(visited_node)
            stack.extend(list(self._g[visited_node].keys())[::-1])
            set_traversed.append(visited_node)
        return set_traversed

    def dijkstra(self):
        """Find the shortest path using Dijksta's algorithm."""

    def bellman_ford(self):
        """Find the shortest path using Bellman-Ford's algorithm."""

if __name__ == '__main__':
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
    print(g.breadth_first_traversal(1))
    print(g.depth_first_traversal(1))
