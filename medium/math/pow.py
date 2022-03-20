
def my_pow(x: float, n: int) -> float:
    '''
     calculates x to the power of n
    '''
    if x == 0:
        return 0

    if n == 0:
        return 1
    return x ** n


# Input: x = 2.00000, n = 10
# Output: 1024.00000
print(my_pow(2.00000, 10))

# Input: x = 2.10000, n = 3
# Output: 9.26100
print(my_pow(2.10000, 3))

# Input: x = 2.00000, n = -2
# Output: 0.25000
print(my_pow(2.00000, -2))