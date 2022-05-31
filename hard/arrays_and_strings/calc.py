
def calculate(s: str) -> int:
    s = s.replace(' ', '')
    code = compile(s, "<string>", "eval")
    return eval(code)


# Input: s = "3+2*2"
# Output: 7
print(calculate("3+2*2"))

# Input: s = " 3/2 "
# Output: 1
print(calculate(" 3/2 "))

# Input: s = " 3+5 / 2 "
# Output: 5
print(calculate(" 3+5 / 2 "))

# "14/3*2"
# Output: 9
# Expected: 8
print(calculate("14/3*2"))
        