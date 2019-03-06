def solution(N, M):
    x = 0
    while x != 1:
        x = N
        y = M
        while y != 0:
            (x, y) = (y, x % y)
        N = N / x
        M = M / x
    return N