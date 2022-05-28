from typing import List

def l(nums: List[int]) -> int:
    answer = list()
    temp = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            temp = nums[i]
            continue
        else:
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                continue
            else:
                answer.append(nums[i])
    return answer

# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
print(l([10,9,2,5,3,7,101,18]))

# Input: nums = [0,1,0,3,2,3]
# Output: 4
# print(l([0,1,0,3,2,3]))

# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# print(l([7,7,7,7,7,7,7]))