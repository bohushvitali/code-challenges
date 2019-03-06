def solution(A):
    length = len(A)

    # array ends can't be peaks, len < 3 must return 0
    if len < 3:
        return 0

    peaks = [0] * length

    # compute a list of 'peaks to the left' in O(n) time
    for index in range(2, length):
        peaks[index] = peaks[index - 1]

        # check if there was a peak to the left, add it to the count
        if A[index - 1] > A[index - 2] and A[index - 1] > A[index]:
            peaks[index] += 1

    # candidate is the block size we're going to test
    for candidate in range(3, length + 1):

        # skip if not a factor
        if length % candidate != 0:
            continue

        # test at each point n / block
        valid = True
        index = candidate
        while index != length:

            # if no peak in this block, break
            if peaks[index] == peaks[index - candidate]:
                valid = False
                break

            index += candidate

        # one additional check since peaks[length] is outside of array
        if index == length and peaks[index - 1] == peaks[index - candidate]:
            valid = False

        if valid:
            return length / candidate

    return 0