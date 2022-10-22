import Heap


class Node:

    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children

    def to_string(self):
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
        self.freq_heap = ObjectHeap([self.ValueFreq(
            node, -value) for node, value in zip(self.tree, self.value_frequency.values())])
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
        min1 = freq_heap.extract_max()
        min2 = freq_heap.extract_max()
        return min1, min2

    def to_string(self):
        return [node.to_string() for node in self.tree]


class ObjectHeap(Heap.MinHeap):

    def heapify_downwards(self, i):
        array = self.heap
        array_size = self.array_size
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        if left <= array_size and array[left].freq > array[i].freq:
            largest = left
        else:
            largest = i

        if right <= array_size and array[right].freq > array[largest].freq:
            largest = right

        if largest != i:
            self.exchange(self.heap, i, largest)
            self.heapify_downwards(largest)

    def heapify_upwards(self, i):
        array = self.heap
        parent = self.get_parent(i)

        if array[parent].freq < array[i].freq and parent >= 0:
            self.exchange(self.heap, parent, i)
            self.heapify_upwards(parent)
