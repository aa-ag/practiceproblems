### GLOBAL
d = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

### FUNCTION(S)
def roman_to_int(s: str) -> int:
    integer = 0

    for i in range(len(s)):
        # check if next character is larger,
        if d[s[i-1]] < d[s[i]]:
            # if it is, must be compound combo
            integer -= d[s[i-1]]
        # else, += to integer
        else:
            integer += d[s[i-1]]

    return integer


### DRIVER
print(roman_to_int('IV'))

# Input: s = "III"
# Output: 3
# print(roman_to_int("III"))

# Input: s = "LVIII"
# Output: 58
# print(roman_to_int("LVIII"))

# Input: s = "MCMXCIV"
# Output: 1994
# print(roman_to_int("MCMXCIV"))