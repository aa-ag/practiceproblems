from typing import List

def moveZeroes(nums: List[int]) -> None:
    '''
     do not return anything: modify in place
    '''

    for i in range(len(nums)):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)



moveZeroes([0,1,0,3,12])
# expected output: [1,3,12,0,0]
moveZeroes([0])
# expected output: [0]ß