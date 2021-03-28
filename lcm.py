# Uses python3
import sys

from test.test import assert_equal


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return int((a * b) // gcd(a, b))


def test_solution():
    assert_equal(24, lcm(6, 8), "6 & 8")
    assert_equal(1933053046, lcm(28851538, 1183019), "28851538 & 1183019")
    assert_equal(46374212988031350, lcm(226553150, 1023473145), "226553150 & 1023473145")


# test_solution()

if __name__ == '__main__':
    input = sys.stdin.read()
    # input = raw_input()
    a, b = map(int, input.split())
    print(lcm(a, b))

