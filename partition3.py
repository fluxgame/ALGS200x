# Uses python3
import sys
import itertools


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0
    # t = []
    # for w in range(0, len(bars) + 1):
    #     t.append([0] * (W + 1))
    #
    # for i in range(1, len(bars) + 1):
    #     for w in range(1, W + 1):
    #         t[i][w] = t[i - 1][w]
    #         if bars[i - 1] <= w:
    #             v = t[i - 1][w - bars[i - 1]] + bars[i - 1]
    #             if v > t[i][w]:
    #                 t[i][w] = v


def partition3Naive(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

