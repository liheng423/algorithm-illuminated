import random


class Vertice:

    def __init__(self):
        pass


class Arc:

    def __init__(self, from_vertice=None, to_vertice=None):
        self.from_vertice = from_vertice
        self.to_vertice = to_vertice

    def random_generator(self):
        pass


class WeightedArc(Arc):

    def __init__(self, from_vertice=None, to_vertice=None, weight=None):
        super().__init__(from_vertice, to_vertice)
        self.weight = weight

    def random_generator(self):
        pass


class WeightedEdge:

    def __init__(self, vertex_set=None, weight=None):
        self.vertex_set = vertex_set
        self.weight = weight

    def random_generator(self, vertex, weight_min, weight_max):
        self.vertex_set = set(random.sample(vertex, 2))
        self.weight = random.randint(weight_min, weight_max)


class Edge:

    def __init__(self, vertex_set):
        self.vertex_set = vertex_set

    def random_generator(self):
        pass


class UndirectedGraph:

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

    def __str__(self):
        return "edges: {0}, \n vertex: {1}".format(self.edges, self.vertex)


def random_graph_generator(num_edges, num_vertex, weight_min, weight_max, vertice_type=Vertice, edge_type=WeightedEdge):
    """

        Args:
            k (int): the number of edges in the desired graph
            num_vertex (int): the number of vertex in the desired graph
            weight_min (int):
            weight_max (int):

        Returns:
            list: generated edges
        """

    # check if the graph is possible to generate
    assert num_edges <= num_vertex * (num_vertex - 1) / 2

    vertex = [vertice_type() for _ in range(num_vertex)]

    # initialize the edge corresponding to edge_init
    edges = []

    # arbiturarily connect the vertex in the graph
    for _ in range(num_edges):

        edge = edge_type()
        while True:
            # sample a new edge from the generator
            edge.random_generator(vertex, weight_min, weight_max)

            # if the edge is not already exsiting in the edge
            if all([edge.vertex_set != existing_edge.vertex_set for existing_edge in edges]):
                edges.append(edge)
                break

    graph = UndirectedGraph(edges, vertex)
    return graph
