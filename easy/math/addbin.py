from email.mime import base


def add_binary(a: str, b: str) -> str:
    return int(a, base=2) + int(b, base=2)

# Input: a = "11", b = "1"
# Output: "100"
print(add_binary("11", "1"))

# Input: a = "1010", b = "1011"
# Output: "10101"
print(add_binary("1010", "1011"))