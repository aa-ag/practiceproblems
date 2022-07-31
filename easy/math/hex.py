def toHex(num: int) -> str:
    return hex(num)[2:]

# Input: num = 26
# Output: "1a"
print(toHex(26))

# Input: num = -1
# Output: "ffffffff"
print(toHex(-1))