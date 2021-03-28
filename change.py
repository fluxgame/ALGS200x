# Uses python3
import sys


def get_change(m):
    if m < 5:
        return m

    if m > 9:
        dimes = m // 10
        return dimes + get_change(m - dimes * 10)

    nickels = m // 5
    return nickels + get_change(m - nickels * 5)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
