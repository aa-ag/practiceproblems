############------------ IMPORTS ------------############
from typing import List
from collections import Counter as count_them


############------------ FUNCTION(S) ------------############
def majority_element(nums: List[int]) -> int:
    return count_them(nums)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # Input: nums = [3,2,3]
    # Output: 3
    print(majority_element([3,2,3]))

    # Input: nums = [2,2,1,1,1,2,2]
    # Output: 2
    print(majority_element([2,2,1,1,1,2,2]))