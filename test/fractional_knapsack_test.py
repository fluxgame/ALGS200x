"""
Sample 1.
Input:
3 50
60 20
100 50
120 30
Output:
180.0000
To achieve the value 180, we take the first item and the third item into the bag.

Sample 2.
Input:
1 10
500 30
Output:
166.6667
Here, we just take one third of the only available item.
"""
from fractional_knapsack import get_optimal_value
from test.asserts import assert_equal

assert_equal("0.0000", "{:.4f}".format(get_optimal_value(0, [20, 50, 30], [60, 100, 120])), "zero capacity")
assert_equal("180.0000", "{:.4f}".format(get_optimal_value(50, [20, 50, 30], [60, 100, 120])), "sample 1")
assert_equal("166.6667", "{:.4f}".format(get_optimal_value(10, [30], [500])), "sample 2")
