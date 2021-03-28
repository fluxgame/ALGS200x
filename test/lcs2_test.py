from lcs2 import lcs2
from test.asserts import assert_equal

assert_equal(2, lcs2([2, 7, 5], [2, 5]), "sample 1")
assert_equal(0, lcs2([2], [1, 2, 3, 4]), "sample 2")
assert_equal(2, lcs2([2, 7, 8, 3], [5, 2, 8, 7]), "sample 3")
