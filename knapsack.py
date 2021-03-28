# Uses python3
import sys


def optimal_weight(W, bars):
    t = []
    for w in range(0, len(bars) + 1):
        t.append([0] * (W + 1))

    for i in range(1, len(bars) + 1):
        for w in range(1, W + 1):
            t[i][w] = t[i - 1][w]
            if bars[i - 1] <= w:
                v = t[i - 1][w - bars[i - 1]] + bars[i - 1]
                if v > t[i][w]:
                    t[i][w] = v

    return t[len(bars)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
