### Increasing Triple Subsequence
from typing import List
import math

def increasing_triplet(nums: List[int]) -> bool:
    '''
      return true if there exists a triple of indices (i, j, k) 
      such that i < j < k and nums[i] < nums[j] < nums[k]
    '''
	# Time Complexity: O(n)
	# Space Complexity: O(1)
    first, second = math.inf, math.inf    
    for i in nums:
		# in example 2, each number is decreasing, so each of those numbers
		# will always be first, none of i + 1 in e.g 2 is greater than its prev i
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True
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