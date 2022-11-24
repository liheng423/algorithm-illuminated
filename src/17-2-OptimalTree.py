import utils.Tree as Tree
import numpy as np


class FreqNode(Tree.Node):

    def __init__(self, value, parent, children, freq):
        super().__init__(value, parent, children)
        self.freq = freq


def get_optimal_BST(nodes,
                    get_freq=lambda x: x.get_freq):
    """
        The Algorithm only accept the nodes list which is ordered in terms of their values.

    Args:
        nodes (_type_): a list of nodes ordered in ascending order.
        get_freq (_type_, optional): a function to get the object's frequency. Defaults to lambdax:x.get_freq.

    Returns:
        _type_: a subproblem table storing all subproblems' optimal results.
    """

    # subproblems initiator:

    length = len(nodes)

    # i from 0, j from 0
    subproblems = np.zeros([length + 1, length + 1])

    # solve all subproblemes (where i <= j)

    # the vertical axis
    for s in range(0, length):
        # the horizontal axis
        for i in range(1, length - s + 1):

            subproblems[i + s, i - 1] = sum([get_freq(node) for node in nodes[i - 1:i + s]]) + min([subproblems[r, i - 1] + subproblems[i + s, r + 1]
                                                                                                    for r in range(i - 1, i + s)])

    return subproblems[-1, 0]
