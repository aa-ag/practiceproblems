from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:    
    d = dict()
    for n1 in nums1:
        d[n1] = d.get(n1, 0) + 1
        
    answer = list()
    for n2 in nums2:
        if n2 in d and d[n2] > 0:
            answer.append(n2)
            d[n2] -= 1
    return answer

# Output: [2,2]
print(intersect([1,2,2,1], [2,2]))

# Output: [4,9]
print(intersect([4,9,5], [9,4,9,8,4]))

# Output [2]
print(intersect([1,2,2,1], [2]))

# Output
print(intersect([2,1], [1,2]))