from typing import List
from collections import Counter


def containsDuplicate(nums: List[int]) -> bool:
    return set(Counter(nums).values()) != {1}


# True
print(containsDuplicate([1,2,3,1]))

# False
print(containsDuplicate([1,2,3,4]))

# True
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))