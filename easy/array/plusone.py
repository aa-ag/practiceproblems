from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return list(digit for digit in str(sum(digits)))


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))