import random


def swap(a, j, i):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp


def search_median_index(array, median, l, r, get_identifier):
    # only in the number of odds

    pivot = random.randint(l, r)
    swap(array, pivot, l)

    i = l + 1

    for j in range(l + 1, r + 1):
        if get_identifier(array[j]) <= get_identifier(array[l]):
            swap(array, i, j)
            i = i + 1

    swap(array, l, i - 1)

    if i - 1 == median:
        return i - 1
    elif i - 1 > median:
        # left
        return search_median_index(array, median, l, i - 2, get_identifier)
    else:
        # right
        return search_median_index(array, median, i, r, get_identifier)


class QuickSort:

    def __init__(self, array, get_identifier=lambda x: x):
        self.array = array
        self.get_identifier = get_identifier
        self._sort(0, len(self.array) - 1)

    def _sort(self, l, r):
        # a is a list
        # l is left endpoint
        # r is right endpoint

        if l >= r:
            # because it operates right on array, theres no need to return anything
            return

        i = self._choose_pivot(l, r)

        swap(self.array, l, i)

        j = self._partition(l, r)

        self._sort(l, j - 1)
        self._sort(j + 1, r)

    def _choose_pivot(self, l, r):
        # choose the pivot, here are different strategies to deploy.

        median = int((l + r) / 2)

        return search_median_index(self.array, median, l, r, self.get_identifier)

    def _partition(self, l, r):
        # this is the pivot
        pivot = self.array[l]
        i = l + 1

        for j in range(l + 1, r + 1):
            # if a[j] > pivot theres nothing happen
            if self.get_identifier(self.array[j]) < self.get_identifier(pivot):
                swap(self.array, j, i)
                # restore invariant
                i += 1

        # place pivot correctly
        swap(self.array, l, i - 1)
        # report final pivot position
        return i - 1
