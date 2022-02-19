### GLOBAL
d = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

### FUNCTION(S)
def roman_to_int(s: str) -> int:
    integer = 0

    if 'IV' in s \
    or 'IX' in s \
    or 'XL' in s \
    or 'XC' in s \
    or 'CD' in s \
    or 'CM' in s:
        for i in range(len(s)):
            if d[s[i-1]] < d[s[i]]:
                integer -= d[s[i-1]]
            else:
                integer += d[s[i-1]]
        return integer
    else:
        for i in range(len(s)):
            integer += d[s[i]]

        return integer


### DRIVER
print(roman_to_int('IV'))
print(roman_to_int('IX'))

# Input: s = "III"
# Output: 3
print(roman_to_int("III"))

# Input: s = "LVIII"
# Output: 58
print(roman_to_int("LVIII"))

# Input: s = "MCMXCIV"
# Output: 1994
print(roman_to_int("MCMXCIV"))