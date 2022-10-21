# All the operations are done by indexing

def quicksort(a, l, r):
    print(a[l:r+1])

    # a is a list
    # l is left endpoint
    # r is right endpoint

    if l >= r:
        # because it operates right on a, theres no need to return anything
        return -1

    i = naive_choosepivot(a, l, r)
    swap(a, l, i)
    j = partition(a, l, r)

    quicksort(a, l, j-1)
    quicksort(a, j+1, r)


def swap(a, j, i):
    temp = a[j]
    a[j] = a[i]
    a[i] = temp
    return -1


def partition(a, l, r):
    p = a[l]  # this is the pivot
    i = l + 1
    for j in range(l+1, r+1):
        if a[j] < p:  # if a[j] > pivot theres nothing happen
            swap(a, j, i)
            i += 1  # restore invariant
    swap(a, l, i - 1)  # place pivot correctly
    return i - 1  # report final pivot position


def naive_choosepivot(a, l, r):
    return l


if __name__ == "__main__":
    a = [3, 2, 5, 6, 1, 4]
    quicksort(a, 0, 5)
    print(a)
