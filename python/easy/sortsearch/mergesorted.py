############------------ IMPORTS ------------############
from typing import List


############------------ FUNCTION(S) ------------############
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    '''
     Merge nums1 and nums2 into a single array
     sorted in non-decreasing order.

     Do not return anything, 
     modify nums1 in-place instead.
    '''
    nums1 = nums1[:m]
    print(nums1)
    nums1 = nums1 + nums2[:n]
    print(nums1)
    nums1.sort()
    print(nums1)


############------------ DRIVER CODE ------------############
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
print(merge([1], 1, [], 0))

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
print(merge([0], 0, [1], 1))