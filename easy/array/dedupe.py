from typing import List


def removeDuplicates(nums: List[int]) -> int:
    return len(list(set(nums)))


# nums = [1,1,2]
# output: 2, nums = [1,2,_]
print(removeDuplicates([1,1,2]))
