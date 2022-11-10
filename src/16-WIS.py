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

    # subproblem
    if n == 0:
        return base_set

    if n == 1:
        base_set.append(graph.vertex[0])
        return base_set

    # recursion when n >= 2
    subproblem_1 = graph.get_subgraph([graph.vertex[-1]])
    subproblem_2 = graph.get_subgraph(graph.vertex[-2:])

    suboptimal_set_1 = recursive_WIS(subproblem_1)
    suboptimal_set_2 = recursive_WIS(subproblem_2)
    suboptimal_set_2.append(graph.vertex[-1])

    return argmax(lambda x: x[1], [(suboptimal_set_1, calc_weights(suboptimal_set_1, lambda x: x.weight)),
                                   (suboptimal_set_2, calc_weights(suboptimal_set_2, lambda x: x.weight))])[0]


def calc_weights(vertex, get_weight):
    if vertex == None:
        return 0
    return sum([get_weight(vertice) for vertice in vertex])


if __name__ == "__main__":
    node0 = WeightedVertice(0, 3)
    node1 = WeightedVertice(1, 2)
    node2 = WeightedVertice(2, 1)
    node3 = WeightedVertice(3, 6)
    node4 = WeightedVertice(4, 4)
    node5 = WeightedVertice(5, 5)

    @timer
    def test():
        return recursive_WIS(WISGraph((Edge({node0, node1}), Edge({node1, node2}), Edge({node2, node3}), Edge({node3, node4}), Edge({node4, node5})),
                                      [node0, node1, node2, node3, node4, node5]))

    print(test(), calc_weights(test(), lambda x: x.weight))  # type: ignore
