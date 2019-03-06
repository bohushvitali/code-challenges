import sys

def solution(A):
    n = len(A)
    left = [0] * n
    for i in xrange(1, n - 1):
        left[i] = max(0, left[i - 1] + A[i])

    right = [0] * n
    for i in xrange(n - 2, 1, -1):
        right[i] = max(0, right[i + 1] + A[i])

    max_sum = -sys.maxint
    for i in xrange(1, n - 1):
        max_sum = max(max_sum, left[i - 1] + right[i + 1])
    return max_sum