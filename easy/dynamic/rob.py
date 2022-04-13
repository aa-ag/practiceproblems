from typing import List

def rob(nums: List[int]) -> int:
    last, now = 0, 0
    for n in nums:
        last, now = now, max(last + n, now)
    return now


# Input: nums = [1,2,3,1]
# Output: 4
print(rob([1,2,3,1]))

# Input: nums = [2,7,9,3,1]
# Output: 12
print(rob([2,7,9,3,1]))