def solution(A):
    n = len(A)
    counter = [0] * n
    for i in range(0, n):
        if (A[i] > 0) and (A[i] <= n):
            counter[A[i] - 1] += 1

    for i in range(0, len(counter)):
        if (counter[i] == 0):
            return i + 1
    return n + 1


def solution(A):
    A.sort()
    A = list(filter(lambda x: x > 0, A))
    n = len(A)
    if n == 0 or A[0] != 1:
        return 1
    for i in xrange(n - 1):
        if A[i + 1] - A[i] > 1:
            return A[i] + 1
    return A[n - 1] + 1