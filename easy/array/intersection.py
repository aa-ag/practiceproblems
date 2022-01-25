from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:    
    answer = list()

    if len(nums1) > len(nums2):
        for i in nums1:
            if i in nums2:
                answer.append(i)
                nums2.remove(i)
        return answer
    elif len(nums1) == len(nums2):
        return [i for i in nums1 if i in nums2]
    else:
        for i in nums2:
            if i in nums1:
                answer.append(i)
                nums2.remove(i)
                nums1.remove(i)
        return answer

# Output: [2,2]
print(intersect([1,2,2,1], [2,2]))

# Output: [4,9]
print(intersect([4,9,5], [9,4,9,8,4]))

# Output [2]
print(intersect([1,2,2,1], [2]))

# Output
print(intersect([2,1], [1,2]))