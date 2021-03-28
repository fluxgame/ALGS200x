# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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


def fibonacci_partial_sum_fast(from_, to):
    partial_sum = fibonacci_sum_fast(to)
    if from_ > 0:
        partial_sum -= fibonacci_sum_fast(from_ - 1)
    return (10 + partial_sum) % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(from_, to))