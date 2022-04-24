# import math

# def sqrt(x: int) -> int:
    # return int(math.sqrt(x))

def sqrt(x: int) -> int:
    l = 0
    h = x

    while l <= h:
        m = (l+h) // 2

        if m*m == x:
            return m
        if m*m > x:
            h = m - 1
        else:
            l = m + 1
    return h

# Input: x = 4
# Output: 2
print(sqrt(4))

# Input: x = 8
# Output: 2
print(sqrt(8))