import queue

# TODO: REFACTORING


def bfs(G, s, q, length):
    vertex, edges, v2e, e2v = G
    done = [s]
    q.put(s)
    while not q.empty():
        v = q.get()
        for edge in v2e[vertex.index(v)]:
            vertex2 = e2v[edges.index(edge)].copy()
            vertex2.remove(vertex.index(v))
            w = vertex2[0]
            if w not in done:
                done.append(w)
                length[w] = length[vertex.index(v)] + 1
                q.put(w)
                print("length:", length)

    return -1


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5, 6]
    edges = [0, 1, 2, 3, 4, 5]
    v2e = [[0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5]]
    e2v = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    length = [-1, -1, -1, -1, -1, -1, -1]

    G = (vertex, edges, v2e, e2v)
    s = 3
    length[s] = 0
    q = queue.Queue(maxsize=100)

    bfs(G, s, q, length)
    print(length)
