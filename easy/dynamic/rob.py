from typing import List

def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    booty = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            booty += nums[i]
    return booty


# Input: nums = [1,2,3,1]
# Output: 4
print(rob([1,2,3,1]))

# Input: nums = [2,7,9,3,1]
# Output: 12
print(rob([2,7,9,3,1]))