
from typing import List
from collections import Counter as c

def find_duplicate(nums: List[int]) -> int:
    return c(nums)
        
# Input: nums = [1,3,4,2,2]
# Output: 2
print(find_duplicate([1,3,4,2,2]))

# Input: nums = [3,1,3,4,2]
# Output: 3
print(find_duplicate([3,1,3,4,2]))