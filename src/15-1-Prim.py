import utils.Graph as Graph
import random
import utils.Heap as Heap
import math
import time


class GroupVertice:

    def __init__(self, key, winner):
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

        assert self._heap is not []

    def run(self):

        # Main Loop

        # if Heap is non-empty
        while self._heap.heap:

            # the default mode is extract max
            opt_vertice = self._heap.extract_min()

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
    weight_max = 1000
    weight_min = 0
    num_vertex = 500
    num_edge = 500*10

    def random_edges_generator(k, num_vertex, weight_min, weight_max):
        """

        Args:
            k (int): the number of edges in the desired graph
            num_vertex (int): the number of vertex in the desired graph
            weight_min (int): 
            weight_max (int): 

        Returns:
            list: generated edges
        """

        assert k <= num_vertex * (num_vertex - 1) / 2

        # initialize the edges list
        edges = []

        for _ in range(k):

            while True:
                append_edge = (((random.randint(0, num_vertex - 1), random.randint(0, num_vertex - 1))),
                               random.randint(weight_min, weight_max))
                if append_edge[0][0] != append_edge[0][1] and set(append_edge[0]) not in [set(edge[0]) for edge in edges]:
                    edges.append(append_edge)
                    break

        return edges

    # prepare the data
    group_vertex = [GroupVertice(None, None) for _ in range(num_vertex)]
    # edges = [((0, 1), 20), ((2, 3), 10), ((0, 2), 5),
    #          ((1, 3), 20), ((0, 3), 15), ((1, 2), 3)]
    edges = random_edges_generator(num_edge, num_vertex, 0, 100)

    weight_edges = [Graph.WeightedEdge(
        {group_vertex[edge_set[0]], group_vertex[edge_set[1]]}, edge_weight)
        for edge_set, edge_weight in edges]

    split_graph = Graph.Graph(weight_edges, group_vertex)

    print("####################RUNNING THE ALGORITHM####################")
    tic = time.time()
    prim = Prim(split_graph)
    MST = prim.run()
    toc = time.time()

    # prettify the result and show

    vertex_dict = dict([(group_vertice, vertice)
                        for vertice, group_vertice in enumerate(group_vertex)])

    # print([(vertex_dict[list(edge.vertex_set)[0]], vertex_dict[list(edge.vertex_set)[1]])
    #       for edge in MST])
    # print(edges)
    print("########### %5.3fs elapsed ###########" % (toc - tic))
