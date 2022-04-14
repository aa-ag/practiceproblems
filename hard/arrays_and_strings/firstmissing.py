from typing import List

def first_missing_positive(nums: List[int]) -> int:
    if all(num < 0 for num in nums):
        return 1
    nums.sort()
    for i in range(1, max(nums) + 2):
        if i not in nums:
            return i


# Input: nums = [1,2,0]
# Output: 3
print(first_missing_positive([1,2,0]))

# Input: nums = [3,4,-1,1]
# Output: 2
print(first_missing_positive([3,4,-1,1]))

# Input: nums = [7,8,9,11,12]
# Output: 1
print(first_missing_positive([7,8,9,11,12]))


# Input: nums = [-5]
# Output: 1
print(first_missing_positive([7,8,9,11,12]))