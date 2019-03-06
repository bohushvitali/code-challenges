def solution(A):
    max_slice = 0
    ret_val = A[0]

    for value in A:
        max_slice = max(value, max_slice + value)
        ret_val = max(ret_val, max_slice)
    return ret_val