from typing import List

def fsc(arr: List[int]) -> int:
    return round(len(arr) * 0.25)


# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6

print(fsc([1,2,2,6,6,6,6,7,10]))

# Input: arr = [1,1]
# Output: 1
print(fsc([1,1]))