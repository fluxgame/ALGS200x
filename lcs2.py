#Uses python3
import sys


def lcs2(a, b):
    ed = [[0] * (len(b) + 1)]
    for i in range(0, len(b) + 1):
        ed[0][i] = i

    for i in range(1, len(a) + 1):
        ed.append([i] + [0] * (len(b)))

    cur_seq = []
    max_seq = 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            diag_latch = ed[i - 1][j - 1]
            if a[i - 1] != b[j - 1]:
                diag_latch += 1
            ed[i][j] = min(ed[i - 1][j] + 1, ed[i][j - 1] + 1, diag_latch)

    for row in ed:
        print(row)
    return max_seq


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
