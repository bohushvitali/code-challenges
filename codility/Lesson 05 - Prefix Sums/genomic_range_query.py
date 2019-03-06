def solution(S, P, Q):
    N = len(S)
    M = len(P)
    result = [0] * M
    pos_of_a = [0] * (N + 1)
    pos_of_c = [0] * (N + 1)
    pos_of_g = [0] * (N + 1)
    pos_of_t = [0] * (N + 1)
    for i in range(0, N):
        if (S[i] == 'A'):
            pos_of_a[i + 1] = 1
        if (S[i] == 'C'):
            pos_of_c[i + 1] = 1
        if (S[i] == 'G'):
            pos_of_g[i + 1] = 1
        if (S[i] == 'T'):
            pos_of_t[i + 1] = 1

    for i in range(1, N + 1):
        pos_of_a[i] += pos_of_a[i - 1]
        pos_of_c[i] += pos_of_c[i - 1]
        pos_of_g[i] += pos_of_g[i - 1]
        pos_of_t[i] += pos_of_t[i - 1]

    for i in range(0, M):
        if ((pos_of_a[Q[i] + 1] - pos_of_a[P[i]]) != 0):
            result[i] = 1
        elif ((pos_of_c[Q[i] + 1] - pos_of_c[P[i]]) != 0):
            result[i] = 2
        elif ((pos_of_g[Q[i] + 1] - pos_of_g[P[i]]) != 0):
            result[i] = 3
        elif ((pos_of_t[Q[i] + 1] - pos_of_t[P[i]]) != 0):
            result[i] = 4
    return result