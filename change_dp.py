# Uses python3
import sys


def get_change(m):
    coins_to_change = [0, 1, 2, 1, 1]
    if m > 4:
        for i in range(5, m + 1):
            minus_one = coins_to_change[i - 1]
            minus_three = coins_to_change[i - 3]
            minus_four = coins_to_change[i - 4]
            coins_to_change.append(1 + min(minus_one, minus_three, minus_four))

    return coins_to_change[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
