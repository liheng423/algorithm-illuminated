from math import floor
from typing import List, TypeVar
import time
import random

T = TypeVar('T')


class MinHeap:

    def __init__(self, array: List[T], get_identifier=lambda x: x):
        self.get_identifier = get_identifier
        self.heap: List[T] = array
        self.array_size: int = len(self.heap) - 1

        # using siftdown strategy
        for i in range(floor(self.array_size / 2), -1, -1):
            self.traverse_downwards(i)

    def comparator(self, x, y):
        """
            This comparator are used to compare two candidates and initialized as minHeap by default.
            If the MaxHeap is needed, then reverse the comparator in this function.
        """
        return self.get_identifier(x) < self.get_identifier(y)

    def traverse_downwards(self, i):
        array = self.heap
        array_size = len(self.heap)
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        if left < array_size and self.comparator(array[left], array[i]):
            largest = left
        else:
            largest = i

        if right < array_size and self.comparator(array[right], array[largest]):
            largest = right

        if largest != i:
            self.exchange(self.heap, i, largest)
            self.traverse_downwards(largest)

    def insert(self, item):
        self.heap.append(item)
        self.traverse_upwards(len(self.heap) - 1)
        return self.heap

    def traverse_upwards(self, i):
        array = self.heap
        parent = self.get_parent(i)

        if not self.comparator(array[parent], array[i]) and parent >= 0:
            self.exchange(self.heap, parent, i)
            self.traverse_upwards(parent)

    def extract_root(self):
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) == 0:
            return min

        self.traverse_downwards(0)
        return min

    def delete(self, i):
        self.heap[i] = self.heap[-1]
        self.heap.pop()

        if len(self.heap) == 0:
            return

        self.traverse_downwards(i)

    def get_root(self) -> T:

        return self.heap[0]  # type: ignore

    @staticmethod
    def exchange(array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        return None

    @staticmethod
    def get_left_child(i):
        # attention: in Python index of array starts at 0.
        return 2 * i + 1

    @staticmethod
    def get_right_child(i):
        return 2 * i + 2

    @staticmethod
    def get_parent(i):
        return floor((i - 1) / 2)


class MaxHeap(MinHeap):

    def comparator(self, x, y):
        return self.get_identifier(x) > self.get_identifier(y)
