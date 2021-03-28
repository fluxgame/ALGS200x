"""
Sample 1.
Input:
1
Output:
0
1

Sample 2.
Input:
5
Output:
3
1 2 4 5
Here, we first multiply 1 by 2 two times and then add 1. Another possibility is to first multiply by 3 and then add 1 two times. Hence “1 3 4 5” is also a valid output in this case.

Sample 3.
Input:
96234
Output:
14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
Again, another valid output in this case is “1 3 9 10 11 33 99 297 891 2673 8019 16038 16039 48117 96234”.
"""
from primitive_calculator import optimal_sequence
from test.asserts import assert_equal

assert_equal([1], optimal_sequence(1), "sample 1")
assert_equal([1, 2, 4, 5], optimal_sequence(5), "sample 2")
assert_equal(
    [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234],
    optimal_sequence(96234), "sample 3"
)
