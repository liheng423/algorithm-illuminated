from UtilsGraph import WeightedArc as Arc
import numpy as np
import UtilsData as Data
from moduletest.Tester import timer as timer


@timer
def bellman_ford(graph, sink, get_weight=lambda x: x.weight):

    n = len(graph.vertex)

    # index represented source
    s = graph.vertex.index(sink)

    # subproblems (i from 0, v indexes V)
    subproblems = np.zeros([n + 1, n])

    # base case (i = 0)
    for vertice in graph.vertex:
        if vertice != sink:
            subproblems[0, vertice - 1] = np.inf

    # solve all subproblems
    # for i from 1 to n
    for i in range(1, n + 1):
        stable = True
        for vertice in graph.vertex:
            # use recurrence
            subproblems[i, vertice - 1] = min(subproblems[i - 1, vertice - 1],
                                              min([subproblems[i - 1, w_vertice - 1] + get_weight(graph.get_edge_by_vertex(vertice, w_vertice))
                                                   for w_vertice in graph.vertex
                                                   if graph.get_edge_by_vertex(vertice, w_vertice) is not None]))
            # check early stopping
            if subproblems[i, vertice - 1] != subproblems[i - 1, vertice - 1]:
                stable = False

        if stable == True:
            return subproblems[i - 1, :]

    # failed to stabilize in n iterations
    return "negative cycle detected!"


if __name__ == "__main__":
    graph = Data.directed_graph_data_loader(
        "/Users/blow/PycharmProjects/Algorithms/testcases/problem18-1.csv")
    print(bellman_ford(graph, 1))
