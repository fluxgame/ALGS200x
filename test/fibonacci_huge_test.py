from fibonacci_huge import get_pisano_period_length, get_fibonacci_huge
from test.asserts import assert_equal


def test_solution():
    assert_equal(8, get_pisano_period_length(3), "pisano of 3")
    assert_equal(6, get_pisano_period_length(4), "pisano of 4")
    assert_equal(20, get_pisano_period_length(5), "pisano of 5")
    assert_equal(60, get_pisano_period_length(10), "pisano of 10")
    assert_equal(1500, get_pisano_period_length(1000), "pisano of 1000")
    assert_equal(1, get_fibonacci_huge(2015, 3), "f(2015) % 3")
    assert_equal(161, get_fibonacci_huge(239, 1000), "f(239) % 1000")
    assert_equal(151, get_fibonacci_huge(2816213588, 239), "f(2816213588) % 239")


test_solution()
