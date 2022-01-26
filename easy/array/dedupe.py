from typing import List


def removeDuplicates(nums: List[int]) -> int:
    return len(list(set(nums)))


# nums = [1,1,2]
# output: 2, nums = [1,2,_]
print(removeDuplicates([1,1,2]))


# nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))