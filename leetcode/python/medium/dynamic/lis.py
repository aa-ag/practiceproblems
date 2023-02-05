from bisect import bisect, bisect_left, bisect_right
from typing import List

def l(nums: List[int]) -> int:
    answer = list()

    for num in nums:
        l = bisect_left(answer, num)
        if l < len(answer):
            answer[l] = num
        else:
            answer.append(num)
    return answer

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
print(l([10,9,2,5,3,7,101,18]))

# Input: nums = [0,1,0,3,2,3]
# Output: 4
print(l([0,1,0,3,2,3]))

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
print(l([7,7,7,7,7,7,7]))