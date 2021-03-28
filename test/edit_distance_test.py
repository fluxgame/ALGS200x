from edit_distance import edit_distance
from test.asserts import assert_equal

assert_equal(0, edit_distance("ab", "ab"), "sample 1")
assert_equal(3, edit_distance("short", "ports"), "sample 2")
assert_equal(5, edit_distance("editing", "distance"), "sample 3")