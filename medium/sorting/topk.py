from ast import operator
from typing import List
from collections import Counter as c

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    d = c(nums)
    return d.most_common(k)[0][0]

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(top_k_frequent([1,1,1,2,2,3], 2))

# Input: nums = [1], k = 1
# Output: [1]
print(top_k_frequent([1], 1))

# Input: [3,0,1,0] 
# Output: [0]
print(top_k_frequent([3,0,1,0], 1))