### Increasing Triple Subsequence
from typing import List

def increasing_triplet(nums: List[int]) -> bool:
    '''
      return true if there exists a triple of indices (i, j, k) 
      such that i < j < k and nums[i] < nums[j] < nums[k]
    '''
    min_firsts = float('inf')
    min_seconds = float('inf')
    
    for num in nums:
        if num > min_seconds:
            return True
        elif num > min_firsts:
            min_seconds = min(min_seconds, num)
        else:
            min_firsts = min(min_firsts, num)
    
    return False


# Input: nums = [1,2,3,4,5]
# Output: true
print(increasing_triplet([1,2,3,4,5]))

# Input: nums = [5,4,3,2,1]
# Output: false
print(increasing_triplet([5,4,3,2,1]))

# Input: nums = [2,1,5,0,4,6]
# Output: true
print(increasing_triplet([2,1,5,0,4,6]))