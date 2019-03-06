def solution(A):
    A_len = len(A)
    if A_len < 3:
        return 0

    A.sort()

    for index in xrange(0, A_len - 2):
        if A[index] + A[index + 1] > A[index + 2]:
            return 1

    return 0