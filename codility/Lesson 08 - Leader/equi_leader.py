def solution(A):
    n = len(A)
    d = dict()
    lv = lk = None
    for i in xrange(n):
        if A[i] not in d:
            d[A[i]] = 1
        else:
            d[A[i]] += 1
        if lv < d[A[i]]:
            lv = d[A[i]]
            lk = A[i]
    if lv <= n / 2:
        return 0
    left = 0
    right = lv
    count = 0
    for i in xrange(n):
        if A[i] == lk:
            left += 1
            right -= 1
        if left > (i + 1) / 2 and right > (n - i - 1) / 2:
            count += 1
    return count