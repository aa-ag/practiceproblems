from typing import List
import itertools

def subsets(nums: List[int]) -> List[List[int]]:
    answer = list()
    for i in range(len(nums)):
        for j in itertools.combinations(nums, i):
            answer.append(list(j))
    
    return answer + [nums]


# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(subsets([1,2,3]))

# Input: nums = [0]
# Output: [[],[0]]
# print(subsets())