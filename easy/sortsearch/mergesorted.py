############------------ IMPORTS ------------############
from typing import List


############------------ FUNCTION(S) ------------############
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    return nums1, m, nums2, n


############------------ DRIVER CODE ------------############
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))