def solution(K, A):
    rope_length = 0
    count = 0

    for num in A:
        rope_length += num
        if rope_length >= K:
            count += 1
            rope_length = 0

    return count