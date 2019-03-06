def solution(nums):
    lefts, rights = sum(nums[:1]), sum(nums[1:])
    minval = abs(lefts - rights)
    for i in range(1, len(nums) - 1):
        lefts += nums[i]
        rights -= nums[i]
        minval = min(minval, abs(lefts - rights))
    return minval