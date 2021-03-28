# Uses python3
import sys

debug_on = False

def debug(str):
    if debug_on:
        print(str)

def find_first_matching_segment(s, p):
    min, max = 0, len(s)

    while min <= max:
        mid = (min + max) // 2;
        debug(f"finding first: p: {p}, s: {s}, min: {min}, max: {max}, mid: {mid}")

        if s[mid][0] <= p <= s[mid][1] and (mid == 0 or (s[mid - 1][0] < p and s[mid - 1][1] < p)):
            debug("point is in the current segment, but not in the previous segment, found first segment!")
            return mid
        if s[mid][0] <= p <= s[mid][1] and s[mid - 1][0] <= p <= s[mid - 1][1]:
            debug("point is in both the current segment and the previous segment, moving back...")
            max = mid - 1
        elif p > s[mid][1]:
            debug("point falls after the current segment, moving forward")
            min = mid + 1;
        elif p < s[mid][1]:
            debug("point falls before the current segment, moving backward")
            max = mid - 1
        if max >= len(s) or min < 0:
            return -1
        debug(f"min: {min}, max: {max}")
    debug("no matching segment found")
    return -1


def find_last_matching_segment(s, p):
    min, max = 0, len(s)

    while min <= max:
        mid = (min + max) // 2;
        debug(f"finding last: p: {p}, s: {s}, min: {min}, max: {max}, mid: {mid}")
        if s[mid][0] <= p <= s[mid][1] and (mid == len(s) - 1 or (p < s[mid + 1][0] and p < s[mid + 1][1])):
            debug("point is in the current segment, but not in the next segment, found last segment!")
            return mid
        if s[mid][0] <= p <= s[mid][1] and s[mid + 1][0] <= p <= s[mid + 1][1]:
            debug("point is in both the current segment and the next segment, moving forward...")
            min = mid + 1
        elif p > s[mid][1]:
            debug("point falls after the current segment, moving forward...")
            min = mid + 1
        elif p < s[mid][0]:
            debug("point falls before the current segment, moving backward...")
            max = mid - 1;
        if max >= len(s) or min < 0:
            return -1
        debug(f"min: {min}, max: {max}")
    debug("no matching end segment found")
    return -1


def fast_count_segments(s, p):
    counts = [0] * len(p)
    s = sorted(s, key=lambda x: (x[0], x[1]))
    debug(s)
    for i in range(0, len(p)):
        first_match = find_first_matching_segment(s, p[i])
        if first_match >= 0:
            counts[i] = find_last_matching_segment(s, p[i]) - first_match + 1

    debug("")
    debug("")
    return counts


def naive_count_segments(segments, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(segments)):
            if segments[j][0] <= points[i] <= segments[j][1]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    segments = []
    for i in range(0, len(starts)):
        segments.append([starts[i], ends[i]])
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(segments, points)
    for x in cnt:
        print(x, end=' ')
