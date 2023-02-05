from typing import List

def plusOne(digits: List[int]) -> List[int]:
    carry  = 1    
    for i in range(len(digits)-1, -1, -1):
        if carry + digits[i] >= 10:
            digits[i] = digits[i] + carry  - 10
            carry = 1
        else:
            digits[i] = digits[i] + 1
            return digits
    if carry:
        digits.insert(0, carry)
    return digits


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))