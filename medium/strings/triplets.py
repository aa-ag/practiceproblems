import enum
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    
    for i,n in enumerate(nums):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l , r = i + 1, len(nums) - 1
        
        while l >= 0 and r < len(nums) and l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                
                res.append([nums[i] , nums[l] , nums[r]])
                l += 1
                while (l > 0 and nums[l] == nums[l - 1] and l < r):
                    l += 1
    return res

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(three_sum([-1,0,1,2,-1,-4]))

# Input: nums = [0,1,1]
# Output: []
print(three_sum([0,1,1]))

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
print(three_sum([0,0,0]))