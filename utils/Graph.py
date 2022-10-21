class Arc:

    def __init__(self, from_vertice, to_vertice):
        self.from_vertice = from_vertice
        self.to_vertice = to_vertice


class WeightedArc(Arc):

    def __init__(self, from_vertice, to_vertice, weight):
        super().__init__(from_vertice, to_vertice)
        self.weight = weight


class WeightedEdge:

    def __init__(self, vertex_set, weight):
        self.vertex_set = vertex_set
        self.weight = weight


class Graph:

    def __init__(self, edges, vertex):
        """
        Args:
            edges (List<Edge>): the key of every edge is the address of the tuple.
            vertex (List<Integer>): the key of every vertice.
        """
        self.edges = edges
        self.vertex = vertex

    def get_edge_by_vertex(self, vertice_1, vertice_2):
        """
        O(m)
        """
        vertex_set = {vertice_1, vertice_2}

        for edge in self.edges:
            if (vertex_set == edge.vertex_set):
                return edge

        return None
