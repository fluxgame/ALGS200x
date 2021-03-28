# Uses python3
import math
import sys


def optimal_sequence(n):
    a = [[0, 0], [0, 0], [1, 1], [1, 3], [2, 2]]
    for i in range(5, n + 1):
        div_two = div_three = [math.inf, math.inf]
        if i % 2 == 0:
            div_two = a[i // 2]
        if i % 3 == 0:
            div_three = a[i // 3]
        minus_one = a[i - 1]
        # print(f"i: {i} /3: {div_three}, /2L {div_two}: -1: {minus_one}")
        min_steps = min(div_two[0], div_three[0], minus_one[0])

        a_i = [min_steps + 1]
        if min_steps == div_three[0]:
            a_i.append(3)
        elif min_steps == div_two[0]:
            a_i.append(2)
        else:
            a_i.append(1)
        # print(i)
        # print(a_i)
        a.append(a_i)

    # print(a)
    sequence = []
    i = n
    while i >= 1:
        sequence.append(i)
        # print(a[i])
        if a[i][1] == 3:
            i = i // 3
        elif a[i][1] == 2:
            i = i // 2
        else:
            i = i - 1
    sequence.reverse()
    return sequence


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
