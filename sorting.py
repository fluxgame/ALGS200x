# Uses python3
import sys
import random
from statistics import median


def partition3(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]

    k = l
    for i in range(l + 1, j + 1):
        if a[i] < x:
            k += 1
            a[i], a[k] = a[k], a[i]

    a[l], a[k] = a[k], a[l]
    return k, j


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def median_pivot(a, l, r):
    mid = l + (r - l) // 2

    median_value = median([a[l], a[mid], a[r]])
    if median_value == a[r]:
        return r
    if median_value == a[l]:
        return l
    return mid


def quick_sort3(a, l, r):
    if l >= r:
        return
    k = median_pivot(a, l, r)
    a[l], a[k] = a[k], a[l]
    m_l, m_r = partition3(a, l, r)
    quick_sort3(a, l, m_l - 1);
    quick_sort3(a, m_r + 1, r);


def quick_sort2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_r, m_l = partition3(a, l, r)
    quick_sort2(a, l, m_l - 1);
    quick_sort2(a, m_r + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
