# Uses python3
import math
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def mark_segments_covered_by(i, segments, segment_status):
    for j in range(0, len(segments)):
        if segments[j].start <= i <= segments[j].end:
            segment_status[j] = 1


def optimal_points(segments):
    left = math.inf
    right = -math.inf
    for s in segments:
        if s.end > right:
            right = s.end
        if s.end < left:
            left = s.end


    points = []
    segment_status = [0] * len(segments)

    while left <= right:
        points.append(left)
        mark_segments_covered_by(left, segments, segment_status)

        left = right + 1
        for i in range(0, len(segments)):
            if segment_status[i] == 0 and segments[i].end <= left:
                left = segments[i].end

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
