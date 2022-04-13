from typing import List
import itertools

def subsets(nums: List[int]) -> List[List[int]]:
    answer = [[]]
    nums.sort()
    for num in nums:
        answer += [i + [num] for i in answer]
    return answer


# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([1,2,3]))

# Input: nums = [0]
# Output: [[],[0]]
print(subsets([0]))