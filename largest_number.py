# Uses python3
import sys


def is_greater_than_or_equal(a, b):
    return a + b > b + a;

def largest_number(a):
    answer = ""
    while len(a) > 0:
        max_num = "-"
        for num in a:
            if is_greater_than_or_equal(num, max_num):
                max_num = num
        answer += max_num
        a.remove(max_num)
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

