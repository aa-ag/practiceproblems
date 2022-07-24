
def is_it(x: int) -> bool:
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    
    r = 0
    while x > r:
        r = r * 10 + x % 10
        x = x // 10

    return True if (x == r or x == r // 10) else False

# true
print(is_it(121))

# false
print(is_it(-121))

# false
print(is_it(10))