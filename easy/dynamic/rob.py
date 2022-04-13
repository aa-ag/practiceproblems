from typing import List

def rob(nums: List[int]) -> int:
    rob_prev = nums[0]
    not_rob_prev = 0

    for num in nums[1:]:
        rob_current = num + not_rob_prev
        not_rob_current = max(rob_prev, not_rob_prev)
        rob_prev, not_rob_prev = rob_current, not_rob_current
    
    return max(rob_prev, not_rob_prev)


# Input: nums = [1,2,3,1]
# Output: 4
print(rob([1,2,3,1]))

# Input: nums = [2,7,9,3,1]
# Output: 12
print(rob([2,7,9,3,1]))