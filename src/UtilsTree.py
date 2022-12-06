class Node:

    def __init__(self, value, parent, children):
        self.value = value
        self.parent = parent
        self.children = children

    def __str__(self):
        return "value: {0}, parent: {1}, children: {2}".format(self.value, self.parent, self.children)


class Tree:

    def __init__(self, nodes):
        self.tree = nodes

    def add_upper_node(self, node):
        self.tree.append(node)

        # update the parent of related node
        node.children[0].parent = node
        node.children[1].parent = node

    def __str__(self):
        return [node.__str__() for node in self.tree]


class RedBlackTree:
    # TODO
    pass
