def solution(A):
    A.sort()

    if A[0] >= 0:
        return A[0] + A[0]
    if A[-1] <= 0:
        return -A[-1] - A[-1]

    front, back = len(A) - 1, 0
    min_abs = A[-1] + A[-1]

    while back <= front:
        temp = abs(A[back] + A[front])

        # Update the result if needed
        if temp < min_abs:
            min_abs = temp

        # Adjust the pointer for next trying
        if abs(A[back + 1] + A[front]) <= temp:
            back += 1
        elif abs(A[back] + A[front - 1]) <= temp:
            front -= 1
        else:
            back += 1
            front -= 1

    return min_abs