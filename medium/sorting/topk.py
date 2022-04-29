from typing import List
from collections import Counter as c

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    answer = list()

    i = 0

    while i < k:
        for k, v in c(nums).items():
            answer.append(k)
            i += 1

    return answer

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(top_k_frequent([1,1,1,2,2,3], 2))


# Input: nums = [1], k = 1
# Output: [1]
print(top_k_frequent([1], 1))