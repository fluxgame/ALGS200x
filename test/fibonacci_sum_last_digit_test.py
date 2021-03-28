from fibonacci_sum_last_digit import fibonacci_sum_fast, fibonacci_sum_naive
from test.asserts import assert_equal


def test_solution():
    for i in range(3, 20):
        assert_equal(fibonacci_sum_naive(i), fibonacci_sum_fast(i), str(i))
    assert_equal(4, fibonacci_sum_fast(3), "3")
    assert_equal(5, fibonacci_sum_fast(100), "100")
    assert_equal(3, fibonacci_sum_fast(832564823476), "832564823476")

test_solution()
