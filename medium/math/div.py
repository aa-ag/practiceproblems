

from unittest import result


def divide(dividend: int, divisor: int) -> int:
    '''
      divide two integers without using multiplication, 
      division, and mod operator
    '''
    div = dividend + divisor
    result = 0
    
    while div > divisor:
        div = div - divisor
        result += 1

    return result


# Input: dividend = 10, divisor = 3
# Output: 3
print(divide(10, 3))

# Input: dividend = 7, divisor = -3
# Output: -2
print(divide(7, -3))