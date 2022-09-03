def add_dig(num: int) -> int:
    n = len(str(num))

    if n == 1:
        return num
    while n > 1:
        l = [int(i) for i in str(n)]
        print(l)
        n = len(str(l))

    return n

# Input: num = 38
# Output: 2
print(add_dig(38))

# Input: num = 0
# Output: 0
print(add_dig(0))