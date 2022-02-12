from typing import List

def moveZeroes(nums: List[int]) -> None:
    '''
     do not return anything: modify in place
    '''
    if len(nums) ==  1 or len(nums) == 0:
            return nums

    if 0 not in nums:
        return nums

    return nums

# moveZeroes([0,1,0,3,12])
# expected output: [1,3,12,0,0]

# moveZeroes([0])
# expected output: [0]

print(moveZeroes([0,0,1]))
# expected output: [1,0,0]