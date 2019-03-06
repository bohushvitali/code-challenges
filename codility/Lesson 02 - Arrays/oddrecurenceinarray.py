def solution(A):
    n = len(A)
    if(A is None or n == 0):
        return 0
    if(n == 1):
        return A[0]
    result = 0
    for i in range(0, n):
        result ^= A[i]
    return result
