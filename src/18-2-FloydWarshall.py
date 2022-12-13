import numpy as np
from UtilsGraph import DirectedGraph
from UtilsGraph import WeightedArc
from typing import Optional
from moduletest.Tester import timer


@timer
def floyd_warshall(graph: DirectedGraph) -> Optional[np.ndarray]:
    INF = 999999
    n = len(graph.vertex)
    subproblems = np.zeros([n + 1, n, n], dtype=np.int_)

    # base case (k = 0)
    for v in range(n):
        for w in range(n):
            edge = graph.get_edge_by_vertex(v, w)
            if v == w:
                subproblems[0, v, w] = 0
            elif edge is not None:
                subproblems[0, v, w] = edge.weight
            else:
                subproblems[0, v, w] = INF

    # systematically solve all subproblems
    for k in range(1, n + 1):
        for v in range(n):
            for w in range(n):
                subproblems[k, v, w] = min(
                    subproblems[k - 1, v, w], subproblems[k - 1, v, k - 1] + subproblems[k - 1, k - 1, w])

    for v in range(n):
        if subproblems[n, v, v] < 0:
            return None

    return subproblems[-1]
