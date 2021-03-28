from inversions import get_number_of_inversions, get_number_of_inversions_naive
from test.asserts import assert_equal

arrays = [[2, 3, 9, 2, 9], [9, 8, 7, 3, 2, 1]]
for a in arrays:
    assert_equal(get_number_of_inversions_naive(a), get_number_of_inversions(a), "sample 3")

"""
9 > 8
9 > 8
9 > 7
9 > 7
9 > 3
9 > 2
9 > 1

8 > 1
8 > 2
8 > 3

8 > 7
8 > 7

7 > 1
7 > 2
7 > 3
7 > 1
7 > 2
7 > 3

3 > 1
3 > 2
3 > 1
3 > 2

2 > 1
2 > 1
"""