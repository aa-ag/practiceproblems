import re

def reformat(number: str) -> str:
    digits = ''.join(i for i in number if i.isdigit())
    return digits


# Input: number = "1-23-45 6"
# Output: "123-456"
print(reformat("1-23-45 6"))

# Input: number = "123 4-567"
# Output: "123-45-67"
print(reformat("123 4-567"))

# Input: number = "123 4-5678"
# Output: "123-456-78
print(reformat("123 4-5678"))