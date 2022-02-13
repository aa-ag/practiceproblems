from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    temp = 0
    answer = list()

    
    for n, num in enumerate(nums):
        if temp < target:
            temp += num
            print(temp)
            answer.append(n)
        else:
            break
    return answer


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
print(twoSum([2,7,11,15], 9))

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# print(twoSum([3,2,4], 6))

# Input: nums = [3,3], target = 6
# Output: [0,1]
# print(twoSum([3,3], 6))