d = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

def roman_to_int(s: str) -> int:
    return s


# Input: s = "III"
# Output: 3
print(roman_to_int("III"))

# Input: s = "LVIII"
# Output: 58
print(roman_to_int("LVIII"))

# Input: s = "MCMXCIV"
# Output: 1994
print(roman_to_int("MCMXCIV"))