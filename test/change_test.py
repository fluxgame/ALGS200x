"""
Sample 1.
Input:
2
Output:
2
2 = 1 + 1.
Sample 2.
Input:
28
Output:
6
28 = 10 + 10 + 5 + 1 + 1 + 1.
"""
from change import get_change
from test.asserts import assert_equal

assert_equal(2, get_change(2), "2")
assert_equal(6, get_change(28), "28")
