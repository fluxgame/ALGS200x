from partition3 import partition3, partition3Naive
from test.asserts import assert_equal

arrays = [
    [3, 3, 3, 3],
    [30],
    [1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]
]

for i in range(0, len(arrays)):
    assert_equal(partition3Naive(arrays[i]), partition3(arrays[i]), "sample " + str(i + 1))
