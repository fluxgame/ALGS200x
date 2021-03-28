from placing_parentheses import get_maximum_value
from test.asserts import assert_equal

assert_equal(6, get_maximum_value("1+5"), "sample 1")
assert_equal(200, get_maximum_value("5-8+7*4-8+9"), "sample 2")