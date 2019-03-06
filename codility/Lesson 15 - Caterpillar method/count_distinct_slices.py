def solution(M, A):
    N = len(A)
    last = 0
    result = 0
    s = [-1] * (M + 1)

    for i, a in enumerate(A):
        if s[a] >= last:
            result += (i - last) * (i - last + 1) / 2
            last = s[a] + 1
            result -= (i - last) * (i - last + 1) / 2

            if result > 1e9:
                return int(1e9)

        s[a] = i

    result += (N - last) * (N - last + 1) / 2
    if result > 1e9:
        return int(1e9)
    return result