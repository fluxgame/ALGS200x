# Uses python3


def edit_distance(s, t):
    ed = [[0] * (len(t) + 1)]
    for i in range(0, len(t) + 1):
        ed[0][i] = i

    for i in range(1, len(s) + 1):
        ed.append([i] + [0] * (len(t)))

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            diag_latch = ed[i - 1][j - 1]
            if s[i - 1] != t[j - 1]:
                diag_latch += 1
            ed[i][j] = min(ed[i - 1][j] + 1, ed[i][j - 1] + 1, diag_latch)
    return ed[len(s)][len(t)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
