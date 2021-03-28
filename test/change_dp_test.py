from change_dp import get_change
from test.asserts import assert_equal

"""
Sample 1.
Input:
2
Output:
2
2 = 1 + 1.
Sample 2.
Input:
34
Output:
9
34 = 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4.
"""

assert_equal(2, get_change(2), "sample 1")
assert_equal(9, get_change(34), "sample 2")
