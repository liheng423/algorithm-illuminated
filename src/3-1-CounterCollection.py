import time


def merge_and_count(c, d):

    i = 0
    j = 0
    inv = 0

    b = []
    for k in range(len(c)+len(d)):
        if i >= len(c):
            b.append(d[j])
            j += 1
            inv += len(c) - i
        elif j >= len(d):
            b.append(c[i])
            i += 1
        elif c[i] < d[j]:
            b.append(c[i])
            i += 1
        else:
            b.append(d[j])
            j += 1
            inv += len(c)-i

    return b, inv


def sort_and_count(a):

    cut = int(len(a)/2)

    if len(a) == 0 or len(a) == 1:
        return a, 0
    else:
        c, inv_l = sort_and_count(a[:cut])
        d, inv_r = sort_and_count(a[cut:])
        b, inv_s = merge_and_count(c, d)
        return b, inv_l + inv_r + inv_s


def brute_force(a):
    inv = 0
    for i in range(len(a)):
        for j in range(i+1):
            if a[i] > a[j]:
                inv += 1
    return inv


if __name__ == '__main__':
    array = range(1000, 0, -1)
    st = time.time()
    _, _ = sort_and_count(array)
    et = time.time()
    print("algo1:", et - st, " sec")

    st = time.time()
    _ = brute_force(array)
    et = time.time()
    print("algo2:", et - st, " sec")


