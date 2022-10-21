import networkx as nx
import matplotlib.pyplot as plt

# TODO: REFACTORING


class Graph:
    def __init__(self, vertex, distance, e2v):
        self._adj = [[] for _ in vertex]
        for i in range(len(e2v)):
            v1, v2 = e2v[i]
            distance_temp = distance[i]
            self._adj[v1].append((v2, distance_temp))
            self._adj[v2].append((v1, distance_temp))

    def get_graph(self):
        return self._adj


def dijkstra(G, s, inf=9999):
    done = [s]
    s_dis = [inf for _ in range(len(G))]
    s_dis[0] = 0
    index = [i for i in range(len(G))]
    not_done = index

    while not_done:
        for i in done:
            arr = G[i]
            for j in range(len(arr)):
                target = arr[j]
                if target[0] in not_done:
                    new_dis = s_dis[i] + target[1]
                    if new_dis < s_dis[target[0]]:
                        s_dis[target[0]] = new_dis
                    # update the info about the iteration
                    done.append(target[0])
                    not_done = list(filter(lambda x: x not in done, index))

    return s_dis


def graph_draw(e2v, distance):
    gra = nx.Graph()
    for i in range(len(e2v)):
        gra.add_edge(*e2v[i], weight=distance[i])

    # positions for all nodes - seed for reproducibility
    pos = nx.spring_layout(gra, seed=7)

    nx.draw_networkx_nodes(gra, pos)
    nx.draw_networkx_edges(gra, pos)
    nx.draw_networkx_labels(gra, pos, font_size=20, font_family="sans-serif")

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5]
    e2v = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5], [0, 5]]
    distance = [10, 2, 4, 2, 1, 10]

    graph = Graph(vertex, distance, e2v)
    G = graph.get_graph()

    dis = dijkstra(G, 0)
    print(dis)

    graph_draw(e2v, distance)
