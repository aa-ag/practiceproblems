from typing import List

def sip(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        l = list(i for i in range(1, max(nums)+1))
        if target > max(l):
            return len(nums)
        else:
            return l.index(target)
            
            


# Input: nums = [1,3,5,6], target = 5
# Output: 2
print(sip([1,3,5,6], 5))

# Input: nums = [1,3,5,6], target = 2
# Output: 1
print(sip([1,3,5,6], 2))

# Input: nums = [1,3,5,6], target = 7
# Output: 4
print(sip([1,3,5,6], 7))