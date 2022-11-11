from utils.Graph import UndirectedGraph as Graph
from utils.Graph import Edge as Edge
from utils.Math import argmax as argmax
from moduletest.Tester import timer


class WeightedVertice:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class WISGraph(Graph):

    def calc_weights(self, get_weight):
        return sum([get_weight(vertice) for vertice in self.vertex])


def recursive_WIS(graph):

    # init
    n = len(graph.vertex)
    base_set = []

    # base cases
    if n == 0:
        return base_set, 0

    if n == 1:
        base_set.append(graph.vertex[0])
        return base_set, graph.vertex[0].weight

    # recursion when n >= 2
    subproblem_1 = graph.get_subgraph([graph.vertex[-1]])
    subproblem_2 = graph.get_subgraph(graph.vertex[-2:])

    suboptimal_set_1, _ = recursive_WIS(subproblem_1)
    suboptimal_set_2, _ = recursive_WIS(subproblem_2)
    suboptimal_set_2.append(graph.vertex[-1])

    return argmax(lambda x: x[1], [(suboptimal_set_1, calc_weights(suboptimal_set_1, lambda x: x.weight)),
                                   (suboptimal_set_2, calc_weights(suboptimal_set_2, lambda x: x.weight))])


def calc_weights(vertex, get_weight):
    if vertex == None:
        return 0
    return sum([get_weight(vertice) for vertice in vertex])


def WIS(graph):

    n = len(graph.vertex)
    sub_solutions = [-1 for _ in range(n + 1)]

    # base cases
    sub_solutions[0] = 0
    sub_solutions[1] = graph.vertex[0].weight

    # caveat: there is difference between the array of vertex and the array of sub_solutions
    for i in range(2, n + 1):
        sub_solutions[i] = max(
            [sub_solutions[i - 1],
             sub_solutions[i - 2] + graph.vertex[i - 1].weight])

    return sub_solutions


def reconstruct(graph, sub_solutions):

    opt_solution = []
    i = len(sub_solutions) - 1

    while i >= 2:
        # not choose the i - 1 vertice
        # NOTICE: sub_solutions[i - 1] represents the vertex[i - 2]
        if sub_solutions[i - 1] >= sub_solutions[i - 2] + graph.vertex[i - 1].weight:
            i -= 1
        else:
            # choose the i - 1 vertice, then we aren't able to choose the i - 2 vertice
            opt_solution.append(graph.vertex[i - 1])
            i -= 2

    if i == 1:
        opt_solution.append(graph.vertex[0])

    return opt_solution


if __name__ == "__main__":
    node0 = WeightedVertice(0, 3)
    node1 = WeightedVertice(1, 2)
    node2 = WeightedVertice(2, 1)
    node3 = WeightedVertice(3, 6)
    node4 = WeightedVertice(4, 4)
    node5 = WeightedVertice(5, 5)

    graph = WISGraph((Edge({node0, node1}), Edge({node1, node2}), Edge({node2, node3}), Edge({node3, node4}), Edge({node4, node5})),
                     [node0, node1, node2, node3, node4, node5])

    @timer
    def test():
        return WIS(graph)

    sub_optimals = test()  # type: ignore
    print(reconstruct(graph, sub_optimals))
    print(sub_optimals[-1])
