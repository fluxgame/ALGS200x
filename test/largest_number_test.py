from largest_number import largest_number, is_greater_than_or_equal
from test.asserts import assert_equal

"""
Sample 1.
Input:
2
21 2
Output:
221
Note that in this case the above algorithm also returns an incorrect answer 212.

Sample 2.
Input:
5
9 4 6 1 9
Output:
99641
In this case, the input consists of single-digit numbers only, so the algorithm above computes the right answer.

Sample 3.
Input:
3
23 39 92
Output:
923923
As a coincidence, for this input the above algorithm produces the right result, though the input does not have any single-digit numbers.

"""
assert_equal(True, is_greater_than_or_equal("2", "21"), "2 is greater than 21")
assert_equal(False, is_greater_than_or_equal("2", "23"), "2 is less than 23")
assert_equal(True, is_greater_than_or_equal("3", "23"), "3 is greater than 23")

assert_equal("221", largest_number(["21", "2"]), "sample 1")
assert_equal("99641", largest_number(["9", "4", "6", "1", "9"]), "sample 2")
assert_equal("923923", largest_number(["23", "39", "92"]), "sample 3")
