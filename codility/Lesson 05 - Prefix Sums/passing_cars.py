def solution(numbers):
    going_east = 0
    passing = 0
    for num in numbers:
        if num == 0:
            going_east += 1
        else:
            passing += going_east
            if passing > 10 ** 9:
                return -1
    return passing