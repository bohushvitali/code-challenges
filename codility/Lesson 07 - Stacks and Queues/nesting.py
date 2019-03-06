def solution(S):
    num_open = 0

    for bracket in S:
        if bracket == '(':
            num_open += 1
        else:
            num_open -= 1

        if num_open < 0:
            return 0

    return 1 if num_open == 0 else 0