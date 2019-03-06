def solution(A, B, C):
    M = len(C)
    N = len(A)

    ELEMENT_MAX_VALUE = 2 * M + 1

    def recursive(begin, end):
        if begin > end:
            return -1
        index = (begin + end + 1) / 2

        nails = ELEMENT_MAX_VALUE * [0]
        for i in xrange(index):
            nails[C[i]] += 1

        partial_sum = ELEMENT_MAX_VALUE * [0]
        partial_sum[0] = nails[0]
        for i in xrange(1, 2 * M + 1):
            partial_sum[i] = partial_sum[i - 1] + nails[i]

        for a, b in zip(A, B):
            if partial_sum[b] - partial_sum[a - 1] == 0:
                break
        else:
            ret = recursive(begin, index - 1)
            return index if ret == -1 else ret

        return recursive(index + 1, end)

    return recursive(0, M)