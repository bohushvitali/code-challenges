def solution(A):
    _dict = {}
    maxA = 0
    for a in A:
        _dict[a] = _dict.get(a, 0) + 1  # count repetitions
        maxA = max(a, maxA)
    ND = [len(A) - 1] * (maxA + 1)
    for b in _dict.keys():
        ND[b] -= (_dict[b] - 1)
        m = b * 2
        while m <= maxA:
            ND[m] -= _dict[b]
            m += b
    result = []
    for a in A:
        result += [ND[a]]
    return result