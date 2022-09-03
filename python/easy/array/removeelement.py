from typing import List

def remove_element(nums: List[int], val: int) -> int:
    try:
        while True: 
            nums.remove(val)
    except:
        pass
    
    return len(nums)


# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
print(remove_element([3,2,2,3],3))

# Input: [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
print(remove_element([0,1,2,2,3,0,4,2],2))