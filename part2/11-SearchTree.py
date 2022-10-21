import random
import time


def swap(array, a, b):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp
    return array


def search_median(array, median, l, r):
    # only in the number of odds
    pivot = random.randint(l, r)
    array = swap(array, pivot, l)
    i = l + 1

    for j in range(l + 1, r + 1):
        if array[j] <= array[l]:
            array = swap(array, i, j)
            i = i + 1
    array = swap(array, l, i - 1)

    if i - 1 == median:
        return array[i - 1]
    elif i - 1 > median:
        # left
        return search_median(array, median, l, i - 2)
    else:
        # right
        return search_median(array, median, i, r)


class SearchTree:
    """
    Search Table Format as follows.
    """

    def __init__(self, array):
        # O(n) to find the median
        median = int(len(array) / 2) - 1
        self.root = search_median(array, median, 0, len(array) - 1)
        array.remove(self.root)

        # generate the initial tree
        self.search_tree = []
        self.search_tree.append([self.root, None, None, None])

        while array:
            item = array.pop()
            self.insert(item)

    def get_parent(self, node):
        return self.search_tree[node][1]

    def get_left_child(self, node):
        return self.search_tree[node][2], 2

    def get_right_child(self, node):
        return self.search_tree[node][3], 3

    def insert(self, item):
        node = 0
        parent = None
        child = None

        while node is not None:
            value = self.search_tree[node][0]
            parent = node

            if item > value:
                node, child = self.get_right_child(node)
            else:
                node, child = self.get_left_child(node)

        # update the the record in the tree
        self.search_tree.append([item, parent, None, None])
        if parent is not None:
            self.search_tree[parent][child] = len(self.search_tree) - 1


if __name__ == "__main__":
    r = 1000
    array = [random.randint(0, r) for _ in range(r)]
    tic = time.time()
    searchTree = SearchTree(array)
    toc = time.time()
    print(f"time elapse {toc - tic} s")
