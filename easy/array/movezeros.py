from typing import List

def moveZeroes(nums: List[int]) -> None:
    '''
     do not return anything: modify in place
    '''
    if len(nums) ==  1:
            return nums

    if 0 not in nums:
        return nums

    zeros = nums.count(0)

    without_zeros = [i for i in nums if i != 0]
    nums = without_zeros + [0] * zeros



# moveZeroes([0,1,0,3,12])
# expected output: [1,3,12,0,0]

# moveZeroes([0])
# expected output: [0]

print(moveZeroes([0,0,1]))
# expected output: [1,0,0]