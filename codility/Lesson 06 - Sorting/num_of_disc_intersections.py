MAX_RESULT = 10 ** 7

def solution(A):
    n = len(A)
    starts = [0] * n
    ends = [0] * n

    # prepare helper arrays
    for i, r in enumerate(A):
        starts[max(i - r, 0)] += 1
        ends[min(i + r, n - 1)] += 1

    active = 0
    intersections = 0

    # sweep away!
    for i, r in enumerate(A):
        started = starts[i]
        ended = ends[i]
        current = active * started + (started * (started - 1) / 2)
        intersections += current
        if intersections > MAX_RESULT:
            return -1
        active += started - ended
    return intersections