from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return ''.join(str(digit) for digit in digits)


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))