from typing import List
from collections import Counter as counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    c = counter(nums1)
    answer = list()
    for n in nums2:
        if c[n] > 0:
            answer.append(n)
            c[n] -= 1
    return answer

# Output: [2,2]
print(intersect([1,2,2,1], [2,2]))

# Output: [4,9]
print(intersect([4,9,5], [9,4,9,8,4]))

# Output [2]
print(intersect([1,2,2,1], [2]))

# Output
print(intersect([2,1], [1,2]))