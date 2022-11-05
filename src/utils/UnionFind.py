"""Supoort Operations

    INITIALIZE: given an array X of objects, create a union-find data structure with each object in its own set.
    FIND: given a union-find data structure and an object x in it, return the name of the set that contains x.
    UNION: given a union-find data strcture and 2 objects in it, merge the sets that contains x, y into a single set.
"""


class Wrapper:

    def __init__(self, item, parent):
        self.item = item
        self.parent = parent
        # to track the size of the union tree
        self.size = 1

    def __str__(self):
        return "item: {0}, parent: {1}, size: {2}".format(self.item, self.parent, self.size)


class UnionFind:
    """
    This data structure is implemented with list.
    key: the position in the list.
    value: an user-defined object containing the parent position it directs to.
    """

    def __init__(self, array) -> None:
        """
        Args:
            array (List<Wrapper(item, parent)>): A list of object desired
        """

        # Perhaps some memeory could be saved.
        self.array = array
        self.wrapper_dict = {item: Wrapper(item, item) for item in array}

    def find(self, target):
        return self._find_wrapper(target).item

    def _find_wrapper(self, target):
        target_wrapper = self.wrapper_dict[target]

        # recursive-based find
        if target_wrapper.item != target_wrapper.parent:
            return self._find_wrapper(target_wrapper.parent)

        # base case
        return target_wrapper

    def union(self, cand1, cand2):
        root1 = self._find_wrapper(cand1)
        root2 = self._find_wrapper(cand2)

        if root1 == root2:
            return

        if root1.size > root2.size:
            # merge the less deep one into the deep one
            root2.parent = root1.item
            root1.size = root1.size + root2.size
        elif root1.size <= root2.size:
            root1.parent = root2.item
            root2.size = root1.size + root2.size
        return

    def __str__(self):
        return str([item.__str__() for item in self.wrapper_dict.values()])


class UnionFindRank(UnionFind):

    """
        Here size is the rank.
    """

    def union(self, cand1, cand2):
        root1 = self._find_wrapper(cand1)
        root2 = self._find_wrapper(cand2)

        if root1 == root2:
            return

        if root1.size > root2.size:
            root2.parent = root1.item
        elif root1.size < root2.size:
            root1.parent = root2.item
        elif root1.size == root2.size:
            root2.parent = root1.item
            root2.size += 1


class UnionFindPathComp(UnionFindRank):

    def _find_wrapper(self, target):
        target_wrapper = self.wrapper_dict[target]

        if target_wrapper.item != target_wrapper.parent:

            # recursive call to attribute all the nodes' parents on the path to the root.
            target_wrapper.parent = self._find_wrapper(target_wrapper.parent)
            return target_wrapper

        # base case
        return target_wrapper
