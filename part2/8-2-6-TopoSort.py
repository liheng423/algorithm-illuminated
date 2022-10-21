# TODO: REFACTORING

def toposort(G):
    global curlabel
    done = []
    vertex, edges, v2e, e2v = G

    curlabel = len(vertex)
    for v in vertex:
        if v not in done:
            dfs_topo(G, v, done)


def get_another(codi, obj):
    for item in codi:
        if item != obj:
            return item


def dfs_topo(G, v, done):
    global curlabel
    global labels
    vertex, edges, v2e, e2v = G
    done.append(v)
    adj = [get_another(x, v) for x in e2v if v in x]
    for ver in adj:
        if ver not in done:
            dfs_topo(G, ver, done)
    labels[ver] = curlabel
    curlabel -= 1


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5, 6]
    labels = [0 for i in range(len(vertex))]
    edges = [0, 1, 2, 3, 4, 5]
    v2e = [[0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5]]
    e2v = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

    G = (vertex, edges, v2e, e2v)

    toposort(G)
