def solution(N):
    result = 0
    if N > 0:
        i = 1
        perimeters = []
        while i * i <= N:
            if N % i == 0:
                perimeters.append(2 * (i + (N / i)))
                i = i + 1
                continue
            i += 1
        result = min(perimeters)
    return result