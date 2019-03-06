def solution(N):
    result = 0
    if N > 0:
        i = 1
        factors = []
        while i**2 <= N:
            if N % i == 0:
                if (N / i) != i:
                    factors.append(i)
                    factors.append(N / i)
                else:
                    factors.append(i)
            i += 1
        result = len(factors)
    return result