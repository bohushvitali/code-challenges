def solution(A):
    if len(A) == 0:
        return -1

    sort_a = sorted(A)
    l = len(A) // 2
    domi_candidate = sort_a[l]
    if A.count(domi_candidate) > l:
        return A.index(domi_candidate)
    return -1