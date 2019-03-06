def solution(nums):
    n = len(nums) + 1
    if n == 1:
        return 1
    expected_sum = (n * (n + 1)) // 2
    return expected_sum - sum(nums)