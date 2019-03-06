def solution(A):
    n = len(A)
    result = 0

    A.sort()

    for first in xrange(n - 2):
        third = first + 2
        for second in xrange(first + 1, n - 1):
            while third < n and A[first] + A[second] > A[third]:
                third += 1
            result += third - second - 1

    return result