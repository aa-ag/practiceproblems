
def is_it(x: int) -> bool:
    if x < 0:
        return False
    else:
        s = str(x)
        return s == s[::-1]

# true
print(is_it(121))

# false
print(is_it(-121))

# false
print(is_it(10))