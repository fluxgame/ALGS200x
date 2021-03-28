from majority_element import get_majority_element, get_majority_element_naive
from test.asserts import assert_equal

arrays = [
    [2, 2, 2, 1],
    [2, 3, 9, 2, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 1],
    [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
]

i = 1
for array in arrays:
    assert_equal(get_majority_element_naive(array), get_majority_element(array, 0, len(array) - 1), f"sample {i}")
    i += 1
