from typing import List 

def sort_colors(nums: List[int]) -> None:
    """
     Do not return anything, modify nums in-place instead.
    """
    left, right = 0, len(nums) - 1
        
    i = 0
        
    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
            i -= 1
        i += 1
    print(nums)


# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
print(sort_colors([2,0,2,1,1,0]))


# Input: nums = [2,0,1]
# Output: [0,1,2]
print(sort_colors([2,0,1]))