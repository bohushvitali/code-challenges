def solution(A, B):
    # No overlapping is possible.
    if len(A) < 2:
        return len(A)

    count = 1
    end = B[0]
    index = 1
    while index < len(A):
        # Skip all the segments in this cluster.
        while index < len(A) and A[index] <= end:
            index += 1

        # All segments are processed.
        if index == len(A):
            break

        # Start a new cluster.
        count += 1
        end = B[index]

    return count