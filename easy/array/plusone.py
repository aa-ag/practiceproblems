from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return int(''.join(str(digit) for digit in digits)) + 1


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))