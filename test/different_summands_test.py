from different_summands import optimal_summands
from test.asserts import assert_equal

"""
Sample 1.
Input:
6
Output:
3
1 2 3

Sample 2.
Input:
8
Output:
3
1 2 5

Sample 3.
Input:
2
Output:
1
2
 """
assert_equal([1, 2, 3], optimal_summands(6), "sample 1")
assert_equal([1, 2, 5], optimal_summands(8), "sample 2")
assert_equal([2], optimal_summands(2), "sample 3")
