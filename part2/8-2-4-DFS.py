
# TODO: REFACTORING

# in python, a list is actually a stack
# with the method called list.pop() and list.append()

def dfs(G, s, stack):
    vertex, edges, v2e, e2v = G
    done = []
    stack.append(s)
    while stack:
        v = stack.pop()
        if v not in done:
            done.append(v)
            print(done)
            adj = [get_another(x, v) for x in e2v if v in x]
            for ver in adj:
                stack.append(ver)

    return -1


def get_another(codi, obj):
    for item in codi:
        if item != obj:
            return item


if __name__ == "__main__":
    vertex = [0, 1, 2, 3, 4, 5, 6]
    edges = [0, 1, 2, 3, 4, 5]
    v2e = [[0], [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5]]
    e2v = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

    G = (vertex, edges, v2e, e2v)
    s = 4
    stack = []

    dfs(G, s, stack)
