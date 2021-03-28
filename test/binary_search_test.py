from binary_search import linear_search, binary_search
from test.asserts import assert_equal

def run_test(a, data):
    for x in data:
        assert_equal(linear_search(a, x), binary_search(a, x), str(x))


run_test([1, 5, 8, 12, 13], [8, 1, 23, 1, 11])
run_test([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
