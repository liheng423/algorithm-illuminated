import queue


# TODO: REFACTORING

def bfs(G, q, s, numCC, cc):
    vertex, edges, v2e, e2v = G
    done = [s]
    q.put(s)
    while not q.empty():
        v = q.get()
        cc[v] = numCC
        for edge in v2e[vertex.index(v)]:
            vertex2 = e2v[edges.index(edge)].copy()
            vertex2.remove(vertex.index(v))
            w = vertex2[0]
            if w not in done:
                done.append(w)
                q.put(w)

    return -1


def ucc(pack, cc):
    vertex = pack[0][0]
    numCC = 0
    done = []
    for i in vertex:  # iterate every vertices
        if i not in done:  # avoid redundancy
            numCC += 1  # new component
            bfs(*pack, s=i, numCC=numCC, cc=cc)


def get_another(codi, obj):
    for item in codi:
        if item != obj:
            return item


def graph_generate(vertex, e2v):
    edges = [i for i in range(len(e2v))]
    v2e = []
    for obj in vertex:
        temp = []
        for i in range(len(e2v)):
            pair = e2v[i]
            if obj in pair:
                temp.append(edges[i])
        v2e.append(temp)

    G = (vertex, edges, v2e, e2v)
    return G


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5, 6]
    e2v = [[0, 2], [2, 4], [3, 5], [4, 6]]
    cc = [-1 for i in range(len(vertex))]

    G = graph_generate(vertex, e2v)
    q = queue.Queue(maxsize=100)
    pack = (G, q)
    ucc(pack, cc)
    print(G)
    print(cc)
