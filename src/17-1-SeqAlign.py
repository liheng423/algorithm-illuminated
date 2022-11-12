
from utils.Math import argmin as argmin


def NW(string_x, string_y, params):

    m = len(string_x)
    n = len(string_y)
    alpha_gap = params["alpha_gap"]
    alpha_matrix = params["alpha_matrix"]

    # subproblem solutions (indexed from 0)
    A = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    # base case #1 (j = 0)
    for i in range(m + 1):
        A[i][0] = i * alpha_gap

    for j in range(n + 1):
        A[0][j] = j * alpha_gap

    # systematically solve all subproblemes
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            A[i][j] = argmin([A[i - 1][j - 1] + alpha_matrix[string_x[i - 1]][string_y[j - 1]],
                              A[i - 1][j] + alpha_gap,
                              A[i][j - 1] + alpha_gap])

    return A


def reconstruct():
    pass


if __name__ == "__main__":

    params = {
        "alpha_gap": 0.6,
        "alpha_matrix": [[0.2, 0.3, 0.4, 0.5] for _ in range(4)]
    }

    print(NW([1, 3, 3], [0, 2, 1, 2], params))
