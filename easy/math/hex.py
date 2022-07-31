def toHex(num: int) -> str:
    return "{0:x}".format(num) if num >= 0 else "{0:x}".format(num + 2 ** 32)

# Input: num = 26
# Output: "1a"
print(toHex(26))

# Input: num = -1
# Output: "ffffffff"
print(toHex(-1))