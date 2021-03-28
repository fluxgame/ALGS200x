# Uses python3
import sys


def fibonacci_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def get_pisano_period_length(m):
    if m == 2:
        return 3

    fib_numbers = [0, 1, 1];

    while True:
        fib_numbers.append((fib_numbers[len(fib_numbers) - 2] + fib_numbers[len(fib_numbers) - 1]) % m)
        if fib_numbers[len(fib_numbers) - 3: len(fib_numbers)] == [0, 1, 1]:
            break;

    return len(fib_numbers) - 3


def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    return fibonacci_fast(n % get_pisano_period_length(m)) % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
