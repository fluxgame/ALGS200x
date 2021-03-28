from dot_product import max_dot_product
from test.asserts import assert_equal
"""
Sample 1.
Input:
1
23
39
Output:
897
897 = 23 · 39. 

Sample 2.
Input:
3
1 3 -5 
-2 4 1
Output:
23
23 = 3 · 4 + 1 · 1 + (−5) · (−2).
"""

assert_equal(897, max_dot_product([23], [39]), "sample 1")
assert_equal(23, max_dot_product([1, 3, -5], [-2, 4, 1]), "sample 2")
