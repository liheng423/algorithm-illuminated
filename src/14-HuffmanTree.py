import UtilsHeap as Heap
import time
import random


class Node:

    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children

    def __str__(self):
        return "value: {0}, parent: {1}, children: {2}".format(self.value, self.parent, self.children)


class Tree:

    def __init__(self, values):
        self.tree = [Node(value, None, (None, None)) for value in values]

    def add_upper_node(self, node):
        self.tree.append(node)

        # update the parent of related node
        node.children[0].parent = node
        node.children[1].parent = node


class HuffmanTree(Tree):
    """
    implemented by Heap
    """

    def __init__(self, value_frequency):
        super().__init__(value_frequency.keys())
        # a variant array storing values and frequencies
        self.value_frequency = value_frequency
        self.freq_heap = Heap.MinHeap([self.ValueFreq(node, value) for node, value in zip(self.tree, self.value_frequency.values())],
                                      lambda x: x.freq)
        self.num_subtree = len(self.tree)

    class ValueFreq:

        def __init__(self, node, freq):
            self.node = node
            self.freq = freq

    def build_huffman_tree(self):
        for _ in range(self.num_subtree - 1):
            children = self.select_best()  # O(logn)
            new_node = Node(children[0].node.value +
                            children[1].node.value, None, children)
            self.add_upper_node(new_node)  # O(1)
            self.freq_heap.insert(self.ValueFreq(
                new_node, children[0].freq + children[1].freq))  # O(logn)

    def select_best(self):

        min1, min2 = self.find_min_heap(self.freq_heap)

        return tuple([min1, min2])

    @staticmethod
    def find_min_heap(freq_heap):
        min1 = freq_heap.extract_root()
        min2 = freq_heap.extract_root()
        return min1, min2

    def __str__(self):
        return [node.__str__() for node in self.tree]


if __name__ == "__main__":
    # value_frequency = {"A": 0.4, "B": 0.25, "C": 0.05, "D": 0.20, "E": 0.1}
    value_frequency = {}
    n = 200
    for i in range(n):
        value_frequency[i] = random.randint(0, 10000)

    tic = time.time()
    bottom_up_tree = HuffmanTree(value_frequency)
    bottom_up_tree.build_huffman_tree()
    toc = time.time()
    # print(bottom_up_tree.to_string())
    print("size: {0}, time elapsed: {1}s".format(n, toc - tic))
