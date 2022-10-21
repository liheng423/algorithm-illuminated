from math import floor
import time
import random


class Heap:

    def __init__(self, array):
        self.heap = array
        self.array_size = len(self.heap) - 1

        # using siftdown strategy
        for i in range(floor(self.array_size / 2), -1, -1):
            self.heapify_downwards(i)

    def heapify_downwards(self, i):
        array = self.heap
        array_size = self.array_size
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        if left <= array_size and array[left] > array[i]:
            largest = left
        else:
            largest = i

        if right <= array_size and array[right] > array[largest]:
            largest = right

        if largest != i:
            self.exchange(self.heap, i, largest)
            self.heapify_downwards(largest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_upwards(len(self.heap) - 1)
        return self.heap

    def heapify_upwards(self, i):
        array = self.heap
        parent = self.get_parent(i)

        if array[parent] < array[i] and parent >= 0:
            self.exchange(self.heap, parent, i)
            self.heapify_upwards(parent)

    def extract_max(self):
        min = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__init__(self.heap)

        return min

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


if __name__ == "__main__":
    # test array goes here
    array = [random.randint(1, 1000) for _ in range(100000)]
    heap = Heap(array)
    tic = time.time()
    heap.insert(1000)
    toc = time.time()
    print(array)
    print(f"time elapses", toc - tic, 's')
