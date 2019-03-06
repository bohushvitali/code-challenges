def solution(X, Y, D):
    distance = Y - X
    result = int(distance / D)
    if distance % D != 0:
        result += 1
    return result