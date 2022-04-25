from typing import List 

def sort_colors(nums: List[int]) -> None:
    """
     Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    
    print(nums)


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
print(sort_colors([2,0,2,1,1,0]))


# Input: nums = [2,0,1]
# Output: [0,1,2]
print(sort_colors([2,0,1]))