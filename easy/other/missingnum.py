from typing import List


def missing_number(nums: List[int]) -> int:
    n = len(nums)
    nums_as_a_set = set(nums)

    for i in range(len(nums)+1):
        if i not in nums_as_a_set:
            return i


# Input: nums = [3,0,1]
# Output: 2
print(missing_number([3,0,1]))

# Input: nums = [0,1]
# Output: 2
print(missing_number([0,1]))

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
print(missing_number([9,6,4,2,3,5,7,0,1]))