import utils.Graph as Graph
import random
import utils.Heap as Heap
import math
from moduletest.Tester import timer


class GroupVertice(Graph.Vertice):

    def __init__(self, key=None, winner=None):
        self.key = key
        self.winner = winner


class Prim:

    def __init__(self, graph):
        self._graph = graph

        self._min_span_tree = []
        self._explored_vertex = []

        # arbitrarily choose the initial vertice
        start = random.choice(graph.vertex)

        # update the unexplored vertex
        self._unexplored_vertex = [
            vertice for vertice in graph.vertex if vertice != start]

        self._explored_vertex.append(start)

        # initilization the keys and winners in terms of vertex
        vertex = self._graph.vertex
        for vertice in vertex:
            edge = graph.get_edge_by_vertex(start, vertice)
            if vertice != start and edge:
                vertice.key = edge.weight
                vertice.winner = edge
            else:
                vertice.key = math.inf
                vertice.winner = None

        self._heap = Heap.MinHeap(self._unexplored_vertex, lambda x: x.key)

        assert self._heap.heap is not []

    def run(self):

        # Main Loop

        # if Heap is non-empty
        while self._heap.heap:

            # the default mode is extract max
            opt_vertice = self._heap.extract_root()

            # add w_opt into the explored node set
            self._explored_vertex.append(opt_vertice)

            # add the local winner edge leading to w_opt to tree
            self._min_span_tree.append(opt_vertice.winner)

            # update keys to maintain invariant
            # likewise in the dijkstra
            for index in range(len(self._unexplored_vertex)):

                # get target vertice from index
                unexplored_vertice = self._unexplored_vertex[index]

                # get edge (opt_vertice, unexplored_vertice)
                edge_probe = self._graph.get_edge_by_vertex(
                    opt_vertice, unexplored_vertice)

                if edge_probe is None:
                    continue

                # check if the edge satisfies the update condition
                if edge_probe.weight < unexplored_vertice.key:
                    self._heap.delete(index)
                    unexplored_vertice.key = edge_probe.weight
                    unexplored_vertice.winner = edge_probe
                    self._heap.insert(unexplored_vertice)

        return self._min_span_tree


if __name__ == "__main__":
    # config
    weight_max = 100
    weight_min = 0
    num_vertex = 20
    num_edge = 19*10

    # prepare the data
    # edges = [((0, 1), 20), ((2, 3), 10), ((0, 2), 5),
    #          ((1, 3), 20), ((0, 3), 15), ((1, 2), 3)]

    graph = Graph.random_graph_generator(
        num_edge, num_vertex, weight_min, weight_max, GroupVertice, Graph.WeightedEdge)

    # main loop of algorithm
    @timer
    def main_loop():
        prim = Prim(graph)
        return prim.run()

    print(main_loop())
    # prettify the result and show

    # vertex_dict = dict([(group_vertice, vertice)
    #                     for vertice, group_vertice in enumerate(group_vertex)])

    # print([(vertex_dict[list(edge.vertex_set)[0]], vertex_dict[list(edge.vertex_set)[1]])
    #       for edge in MST])
    # print(edges)
