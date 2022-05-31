
def calculate(s: str) -> int:
    return eval(s)


# Input: s = "3+2*2"
# Output: 7
print(calculate("3+2*2"))

# Input: s = " 3/2 "
# Output: 1
print(calculate(" 3/2 "))

# Input: s = " 3+5 / 2 "
# Output: 5
print(calculate(" 3+5 / 2 "))

        