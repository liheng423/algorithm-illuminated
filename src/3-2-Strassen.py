import time


def naive(x, y):

    # O(n^3)

    z = []

    for i in range(len(x)):
        row = []
        for j in range(len(y)):
            entry = 0
            for k in range(len(y)):
                entry += x[i][k] * y[k][j]
            row.append(entry)
        z.append(row)
    return z


def add(x, y):
    n = len(x)
    return [[x[i][j] + y[i][j] for j in range(n)] for i in range(n)]

# assumption: n is a power of 2


def recmatmult(x, y):
    # O(n^3)
    n = len(x)
    # base case
    if n == 1:
        return [[x[0][0]*y[0][0]]]
    else:
        a, b, c, d = submat(x)
        e, f, g, h = submat(y)
        # here goes recursively

        z = [[]for i in range(n)]
        # here is 8 recursive calls
        z1 = add(recmatmult(a, e), recmatmult(b, g))
        z2 = add(recmatmult(a, f), recmatmult(b, h))
        z3 = add(recmatmult(c, e), recmatmult(d, g))
        z4 = add(recmatmult(c, f), recmatmult(d, h))

        for i in range(n):
            for j in range(n):
                if i < n/2 and j < n/2:
                    z[i].append(z1[i][j])
                elif i < n/2 <= j:
                    z[i].append(z2[i][j-n//2])
                elif i >= n/2 > j:
                    z[i].append(z3[i-n//2][j])
                else:
                    z[i].append(z4[i-n//2][j-n//2])
        return z

def strassen(x, y):
    # O(n^log_2 7)
    n = len(x)
    # base case
    if n == 1:
        return [[x[0][0]*y[0][0]]]
    else:
        a, b, c, d = submat(x)
        e, f, g, h = submat(y)
        # here goes recursively

        z = [[]for i in range(n)]
        # here is 8 recursive calls
        p1 = strassen(a, add(f, [[-1*h[i][j] for j in range(n//2)]for i in range(n//2)]))
        p2 = strassen(add(a, b), h)
        p3 = strassen(add(c, d), e)
        p4 = strassen(d, add(g, [[-1*e[i][j] for j in range(n//2)]for i in range(n//2)]))
        p5 = strassen(add(a, d), add(e, h))
        p6 = strassen(add(b, [[-1*d[i][j] for j in range(n//2)]for i in range(n//2)]), add(g, h))
        p7 = strassen(add(a, [[-1*c[i][j] for j in range(n//2)]for i in range(n//2)]), add(e, f))

        z1 = add(add(add(p5, p4),
                     [[-1 * p2[i][j] for j in range(n // 2)] for i in range(n // 2)]), p6)
        z2 = add(p1, p2)
        z3 = add(p3, p4)
        z4 = add(add(add(p1, p5),
                     [[-1 * p3[i][j] for j in range(n // 2)] for i in range(n // 2)]),
                 [[-1 * p7[i][j] for j in range(n // 2)] for i in range(n // 2)])

        for i in range(n):
            for j in range(n):
                if i < n/2 and j < n/2:
                    z[i].append(z1[i][j])
                elif i < n/2 <= j:
                    z[i].append(z2[i][j-n//2])
                elif i >= n/2 > j:
                    z[i].append(z3[i-n//2][j])
                else:
                    z[i].append(z4[i-n//2][j-n//2])
        return z



def submat(x):
    n = len(x)

    a = [[x[k][i] for i in range(0, n//2)] for k in range(0, n//2)]
    b = [[x[k][i] for i in range(n//2, n)] for k in range(0, n//2)]
    c = [[x[k][i] for i in range(0, n//2)] for k in range(n//2, n)]
    d = [[x[k][i] for i in range(n//2, n)] for k in range(n//2, n)]

    return a, b, c, d


if __name__ == "__main__":

    # INITIALIZATION
    n = 128
    x = [[i for i in range(n)] for k in range(n)]
    y = [[i for i in range(n)] for k in range(n)]
    print(f"=====test n={n}=======")
    st = time.time()
    z1 = naive(x, y)
    et = time.time()
    print("naive:", et - st, " sec")

    st = time.time()
    z2 = strassen(x, y)
    et = time.time()
    print("strassen:", et - st, " sec")
    print(z1 == z2)
    print("we find that the result is much worse than the original one")

