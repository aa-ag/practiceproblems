
def divide(dividend: int, divisor: int) -> int:
    '''
      divide two integers without using multiplication, 
      division, and mod operator
    '''
    remainder = dividend
    quotient = 0

    while remainder >= divisor:
        remainder = remainder - divisor
        quotient += 1

    return quotient


# Input: dividend = 10, divisor = 3
# Output: 3
print(divide(10, 3))

# Input: dividend = 7, divisor = -3
# Output: -2
print(divide(7, -3))