# Uses python3
import sys


def get_number_of_inversions_naive(a):
    count = 0
    for i in range(0, len(a)):
        for j in range (0, len(a)):
            if i < j and a[i] > a[j]:
                count += 1
    return count


def merge(l, r, a):
    number_of_inversions = i = j = k = 0

    # print(f"pre-merge: {a}, l: {l}, r: {r}")
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            # print(f"{l[i]} > {r[j]}")
            # print(f"swapping {r[j]} and {a[k]}")
            # print(f"copy {r[j]} from r[{j}] to a[{k}]")
            a[k] = r[j]
            j += 1
            number_of_inversions += (len(l) - i)
        k += 1
        # print(f"post-merge: {a}, l: {l}, r: {r}")

    while i < len(l):
        a[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        a[k] = r[j]
        j += 1
        k += 1
    return number_of_inversions


def get_number_of_inversions(a):
    number_of_inversions = 0
    if len(a) <= 1:
        return number_of_inversions
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    number_of_inversions += get_number_of_inversions(left)
    number_of_inversions += get_number_of_inversions(right)
    number_of_inversions += merge(left, right, a)
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a))
