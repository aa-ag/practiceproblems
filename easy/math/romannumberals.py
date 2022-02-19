### GLOBAL
d = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

### FUNCTION(S)
def roman_to_int(s: str) -> int:
    integer = 0

    for i in range(len(s) -1):
        if d[s[i]] >= d[s[i+1]]:
            integer += d[s[i]]
            # print(integer)
        else:
            integer -= d[s[i]]
            # print(integer)

    return integer + d[s[-1]]


### DRIVER
print(roman_to_int('IV')) # 4
print(roman_to_int('IX')) # 9
print(roman_to_int("III")) # 3
print(roman_to_int("LVIII")) # 58
print(roman_to_int("MCMXCIV")) # 1994