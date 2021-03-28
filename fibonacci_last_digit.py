# Uses python3
import sys

from test.test import assert_equal


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fibonacci_fast(n):
    if n <= 1:
        return n

    fib_numbers = [0, 1]

    for i in range(2, n + 1):
        fib_numbers.append(fib_numbers[i - 1] + fib_numbers[i - 2])

    return fib_numbers[n] % 10


def test_solution():
    assert_equal(2, fibonacci_fast(3), "3")
    assert_equal(5, fibonacci_fast(10), "55")
    assert_equal(1, fibonacci_fast(239), "239")

    for n in range(0, 20):
        assert_equal(get_fibonacci_last_digit_naive(n), fibonacci_fast(n), n)


if __name__ == '__main__':
    # test_solution()
    print(fibonacci_fast(int(sys.stdin.read())))
