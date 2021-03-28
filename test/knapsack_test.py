from knapsack import optimal_weight
from test.asserts import assert_equal

assert_equal(9, optimal_weight(10, [1, 4, 8]), "sample 1")
assert_equal(9, optimal_weight(10, [8, 4, 1]), "sample 1, reversed")
