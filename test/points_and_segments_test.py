from points_and_segments import naive_count_segments, fast_count_segments
from test.asserts import assert_equal

segments = [
    [[0, 5], [7, 10]],
    [[-10, 10]],
    [[0, 5], [-3, 2], [7, 10]]
]
bets = [[1, 6, 11], [-100, 100, 0], [1, 6]]

for i in range(0, len(segments)):
    assert_equal(
        naive_count_segments(segments[i], bets[i]),
        fast_count_segments(segments[i], bets[i]),
        f"sample {i + 1}"
    )
