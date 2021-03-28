from fibonacci_partial_sum import fibonacci_partial_sum_fast
from test.asserts import assert_equal


def test_solution():
    assert_equal(0, fibonacci_partial_sum_fast(0, 0), "0...0")
    assert_equal(1, fibonacci_partial_sum_fast(3, 7), "3...7")
    assert_equal(5, fibonacci_partial_sum_fast(10, 10), "10...10")
    assert_equal(2, fibonacci_partial_sum_fast(10, 200), "10...200")
    assert_equal(5, fibonacci_partial_sum_fast(1, 100000000), "1...100000000")

test_solution()
