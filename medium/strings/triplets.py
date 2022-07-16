import enum
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
        triples = []
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                triples.extend(two_sum(nums, i))
        return triples
    
def two_sum(nums: List[int], i: int) -> List[List[int]]:
    triples = []
    
    j, k = i + 1, len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == 0:
            triples.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
            while j < k and nums[k] == nums[k+1]:
                k -= 1
        elif total < 0:
            j += 1
        else:
            k -= 1
            
    return triples

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
print(three_sum([-1,0,1,2,-1,-4]))

# Input: nums = [0,1,1]
# Output: []
print(three_sum([0,1,1]))

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
print(three_sum([0,0,0]))