from contextlib import suppress
from inspect import isclass
import random
from typing import Set

from pyparsing import Suppress


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


class Edge:

    def __init__(self, vertex_set):
        self.vertex_set = vertex_set

    def random_generator(self):
        pass


class WeightedEdge(Edge):

    def __init__(self, vertex_set=None, weight=None):
        super().__init__(vertex_set)
        self.weight = weight

    def random_generator(self, vertex, weight_min, weight_max):
        self.vertex_set = set(random.sample(vertex, 2))
        self.weight = random.randint(weight_min, weight_max)

    def __str__(self):
        return "vertex_set: {0}, weight: {1}".format(self.vertex_set, self.weight)


class Graph:

    def __init__(self, edges, vertex):
        """
        Args:
            edges (List<Edge>): the key of every edge is the address of the tuple.
            vertex (List<Integer>): the key of every vertice.
        """
        self.edges = edges
        self.vertex = vertex


class DirectedGraph(Graph):

    def get_edge_by_vertex(self, from_vertice, to_vertice):

        for edge in self.edges:
            if (edge.from_vertice == from_vertice and edge.to_vertice == to_vertice):
                return edge

        return None

    def add_arc(self, arc: Arc):

        if arc.from_vertice not in self.vertex:
            self.vertex.append(arc.from_vertice)

        if arc.to_vertice not in self.vertex:
            self.vertex.append(arc.to_vertice)

        if arc not in self.edges:
            self.edges.append(arc)
            return True
        return False


class UndirectedGraph(Graph):

    def get_edge_by_vertex(self, vertice_1, vertice_2):
        """
        O(m)
        """
        vertex_set = {vertice_1, vertice_2}

        for edge in self.edges:
            if (vertex_set == edge.vertex_set):
                return edge

        return None

    # TODO: This method can be optimized
    def get_subgraph(self, vertex_exclude):

        vertex = list(
            filter(lambda x: x not in vertex_exclude, self.vertex))
        edges = list(filter(lambda x: not (
            list(x.vertex_set)[0] in vertex_exclude) and not (list(x.vertex_set)[1] in vertex_exclude), self.edges))

        return self.__class__(edges, vertex)

    def add_edge(self, edge: Edge):

        first_vertice = list(edge.vertex_set)[0]
        second_vertice = list(edge.vertex_set)[1]

        if first_vertice not in self.vertex:
            self.vertex.append(first_vertice)

        if second_vertice not in self.vertex:
            self.vertex.append(second_vertice)

        if edge not in self.edges:
            self.edges.append(edge)
            return True
        return False

    def add_vertice(self, vertice):
        if vertice not in self.vertex:
            self.vertex.append(vertice)
            return True
        return False

    def __str__(self):
        return "edges: {0}, \n vertex: {1}".format([edge.__str__() for edge in self.edges], self.vertex)


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


def prettify_edges_output(vertex, edges_output):

    # create a hashmap to mirror every vertice object to int type
    vertex_dict = {key: value for value, key in enumerate(vertex)}

    return [((vertex_dict[list(edge.vertex_set)[0]], vertex_dict[list(edge.vertex_set)[1]]), edge.weight) for edge in edges_output]
