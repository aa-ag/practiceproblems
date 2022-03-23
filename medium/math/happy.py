############------------ FUNCTION(S) ------------############
def is_happy(n: int) -> bool:
    '''
     1 <= n <= 231 - 1
     code from https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-66.php
    '''
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