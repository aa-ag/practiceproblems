from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# Input: nums = [2,5,5,11], target = 10
# Output: [1,2]
print(twoSum([2,5,5,11], 10))

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
print(twoSum([2,7,11,15], 9))

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
print(twoSum([3,2,4], 6))

# Input: nums = [3,3], target = 6
# Output: [0,1]
print(twoSum([3,3], 6))