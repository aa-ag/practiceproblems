from typing import List

def moveZeroes(nums: List[int]) -> None:
    '''
     do not return anything: modify in place
    '''
    if len(nums) ==  1 or len(nums) == 0:
            return nums

    if 0 not in nums:
        return nums
    
    count = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    for j in range(count, len(nums)):
        nums[j] = 0

    return nums

# moveZeroes([0,1,0,3,12])
# expected output: [1,3,12,0,0]

# moveZeroes([0])
# expected output: [0]

print(moveZeroes([0,0,1]))
# expected output: [1,0,0]