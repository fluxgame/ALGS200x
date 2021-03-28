# Uses python3
import math


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    n = (len(dataset) - 1) // 2 + 1
    mins = [[0] * (n + 1)]
    maxes = [[0] * (n + 1)]
    opers = [""]
    for ri in range(1, n + 1):
        mins.append([0] * (n + 1))
        maxes.append([0] * (n + 1))
        maxes[ri][ri] = mins[ri][ri] = int(dataset[(ri - 1) * 2])
        if ri < n:
            opers.append(dataset[(ri - 1) * 2 + 1])

    for ci in range(2, n + 1):
        for ri in range(ci - 1, 0, -1):
            mins[ri][ci] = math.inf
            maxes[ri][ci] = -math.inf
            for i in range(ri, ci):
                v1 = evalt(maxes[ri][i], maxes[i + 1][ci], opers[i])
                v2 = evalt(maxes[ri][i], mins[i + 1][ci], opers[i])
                v3 = evalt(mins[ri][i], maxes[i + 1][ci], opers[i])
                v4 = evalt(mins[ri][i], mins[i + 1][ci], opers[i])
                mins[ri][ci] = min(mins[ri][ci], v1, v2, v3, v4)
                maxes[ri][ci] = max(maxes[ri][ci], v1, v2, v3, v4)

    return maxes[1][n]


if __name__ == "__main__":
    print(get_maximum_value(input()))
