# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)
        sum += current

    return sum % 10


def fibonacci_sum_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    pisano = 60     # pisano period of 10 is 60

    for _ in range((n % pisano) + 1):
        previous, current = current, (previous + current) % 10

    return (10 + current - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
