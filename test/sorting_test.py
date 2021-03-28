from sorting import quick_sort3, quick_sort2
from test.asserts import assert_equal

i = 2
arrays = [[2, 3, 9, 2, 2], [2, 3, 9, 2, 9], [3] * i + [2] * i + [1] * i]

for a in arrays:
    q2 = a.copy()
    q3 = a.copy()
    quick_sort2(q2, 0, len(a) - 1)
    quick_sort3(q3, 0, len(a) - 1)
    print(a)
    print(q2)
    print(q3)
    assert_equal(q2, q3, str(a))
