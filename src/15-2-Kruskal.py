from threading import get_ident
from numpy import get_include
from moduletest.Tester import timer
from UtilsUnionFind import UnionFindRank
import UtilsGraph as Graph
from UtilsSorter import QuickSort

"""
    Union-Find-Based Kruskal
    The union find data structure here is to avoid any cycle in the graph.
"""


class Kruskal:

    def __init__(self, graph):
        self._min_span_tree = []
        self._graph = graph
        self._union_find = UnionFindRank(graph.vertex)
        quick_sort = QuickSort(graph.edges, get_identifier=lambda x: x.weight)
        self.sorted_edges = quick_sort.array

    # Main Loop
    def run(self):

        for edge in self.sorted_edges:
            vertice1 = list(edge.vertex_set)[0]
            vertice2 = list(edge.vertex_set)[1]
            if self._union_find.find(vertice1) != self._union_find.find(vertice2):
                # no ver1-ver2 path in T, ok to add (ver1, ver2)
                self._min_span_tree.append(edge)
                self._union_find.union(vertice1, vertice2)

        return self._min_span_tree


if __name__ == "__main__":
    # config
    weight_max = 1000
    weight_min = 0
    num_vertex = 100
    num_edge = 50*99

    graph = Graph.random_graph_generator(
        num_edge, num_vertex, weight_min, weight_max)

    @timer
    def main_loop():
        kruskal = Kruskal(graph)
        return kruskal.run()

    print(Graph.prettify_edges_output(graph.vertex, main_loop()))
