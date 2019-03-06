def solution(count, operations):
    n = count + 1
    counters = [0] * n
    oldcmax = cmax = 0
    for idx in operations:
        if idx == count + 1:
            oldcmax = cmax
        else:
            if counters[idx] < oldcmax:
                counters[idx] = oldcmax
            counters[idx] += 1
            if counters[idx] > cmax:
                cmax = counters[idx]
    return [max(num, oldcmax) for num in counters[1:]]