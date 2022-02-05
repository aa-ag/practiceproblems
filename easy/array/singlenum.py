from typing import List
from collections import Counter as c

def singleNumber(nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))