from math import floor
import time
import random


class MinHeap:

    def __init__(self, array, get_value=lambda x: x):
        self.get_value = get_value
        self.heap = array
        self.array_size = len(self.heap) - 1

        # using siftdown strategy
        for i in range(floor(self.array_size / 2), -1, -1):
            self.traverse_downwards(i)

    def traverse_downwards(self, i):
        array = self.heap
        array_size = len(self.heap)
        left = self.get_left_child(i)
        right = self.get_right_child(i)
        if left < array_size and self.get_value(array[left]) < self.get_value(array[i]):
            largest = left
        else:
            largest = i

        if right < array_size and self.get_value(array[right]) < self.get_value(array[largest]):
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

        if self.get_value(array[parent]) > self.get_value(array[i]) and parent >= 0:
            self.exchange(self.heap, parent, i)
            self.traverse_upwards(parent)

    def extract_min(self):
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


# if __name__ == "__main__":
#     # test array goes here
#     array = [random.randint(1, 1000) for _ in range(100000)]
#     heap = Heap(array)
#     tic = time.time()
#     heap.insert(1000)
#     toc = time.time()
#     print(array)
#     print(f"time elapses", toc - tic, 's')
