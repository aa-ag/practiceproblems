from typing import List

def fmx(nums: List[int]) -> int:
    groups = list()
    temp = 0

    for num in nums:
        if num == 1:
            temp += 1
        else:
            groups.append(temp)
            temp = 0
    groups.append(temp)
    return max(groups)


# Input: nums = [1,1,0,1,1,1]
# Output: 3
print(fmx([1,1,0,1,1,1]))

# Input: nums = [1,0,1,1,0,1]
# Output: 2
print(fmx([1,0,1,1,0,1]))