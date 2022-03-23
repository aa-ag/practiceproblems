############------------ FUNCTION(S) ------------############
def is_happy(n: int) -> bool:
    check = set()
    while n != 1:
        res = 0
        while n:
            res += (n % 10)**2
            n //= 10
        n = res
        if n in check:
            return False
        else:
            check.add(n)
    return True

############------------ DRIVER CODE ------------############
# Input: n = 19
# Output: true
print(is_happy(19))

# Input: n = 2
# Output: false
print(is_happy(2))