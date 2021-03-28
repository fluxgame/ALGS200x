# Uses python3
import sys


def get_majority_element_naive(a):
    for i in range(0, len(a)):
        current = a[i]
        count = 0
        for j in range(0, len(a)):
            if a[j] == current:
                count += 1
        if count > len(a) / 2:
            return a[i]
    return -1


def count_in_range(a, num, left, right):
    count = 0
    for i in range(left, right + 1):
        if a[i] == num:
            count += 1
    return count


def get_majority_element(a, left, right):
    if left > right:
        return -1

    if left == right:
        return a[left]

    mid = left + (right - left) // 2
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid + 1, right)

    if right_majority == left_majority:
        return right_majority

    left_count = right_count = 0
    if left_majority >= 0:
        left_count = count_in_range(a, left_majority, left, right)

    if right_majority >= 0:
        right_count = count_in_range(a, right_majority, left, right)

    if left_count > (right - left + 1) / 2:
        return left_majority
    if right_count > (right - left + 1) / 2:
        return right_majority
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, len(a) - 1) != -1:
        print(1)
    else:
        print(0)
