from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if len(nums) == 0: 
            return 0
    elif len(nums) == 1: 
        return 1
    else:
        left = 1
        for right in range(1, len(nums)):
            if nums[right - 1] == nums[right]: 
                pass
            else:
                nums[left] = nums[right]
                left += 1
        return left


# nums = [1,1,2]
# output: 2, nums = [1,2,_]
print(removeDuplicates([1,1,2]))


# nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


# nums = [1,1,2]
# output: [1, 2]
print(removeDuplicates([1,1,2]))