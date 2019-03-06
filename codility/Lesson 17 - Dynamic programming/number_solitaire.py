def solution(A):
    for i in range(1, len(A)):
        A[i] = A[i] + max(A[max(0, i - 6): i])
    return A[-1]