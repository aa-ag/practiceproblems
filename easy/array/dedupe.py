from typing import List


def removeDuplicates(nums: List[int]) -> int:
    nums = sorted(set(nums))
    return nums


# nums = [1,1,2]
# output: 2, nums = [1,2,_]
print(removeDuplicates([1,1,2]))


# nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


# nums = [1,1,2]
# output: [1, 2]
print(removeDuplicates([1,1,2]))