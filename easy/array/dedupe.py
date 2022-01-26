from typing import List


def removeDuplicates(nums: List[int]) -> int:
    k = 0
    unique = list()
    for num in nums:
        if num not in unique:
            unique.append(num)
            k += 1
        else:
            continue
    return k


# nums = [1,1,2]
# output: 2, nums = [1,2,_]
print(removeDuplicates([1,1,2]))


# nums = [0,0,1,1,1,2,2,3,3,4]
# output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


# nums = [1,1,2]
# output: [1, 2]
print(removeDuplicates([1,1,2]))