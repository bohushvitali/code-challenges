def solution(nums):
    """Check if given nums are permutation 1..N."""
    if not nums:
        return 0
    seen = set()
    for num in nums:
        if num < 1 or num > len(nums) or num in seen:
            return 0
        seen.add(num)
    return 1