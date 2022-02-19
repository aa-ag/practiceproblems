### GLOBAL
d = {
    "I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000
}

### FUNCTION(S)
def roman_to_int(s: str) -> int:
    d = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400, 
        "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, 
        "IX": 9, "V": 5, "IV": 4, "I": 1
    }
    previous_character = 0
    final_answer = 0

    for character in s:
        current_value = d[character]
        final_answer += current_value

        if previous_character < current_value:
            final_answer -= 2 * previous_character

        previous_character = current_value
    
    return final_answer

# def roman_to_int(s: str) -> int:
#     integer = 0

#     for i in range(len(s) -1):
#         if d[s[i]] >= d[s[i+1]]:
#             integer += d[s[i]]
#         else:
#             integer -= d[s[i]]

#     return integer + d[s[-1]]


### DRIVER
print(roman_to_int('IV')) # 4
print(roman_to_int('IX')) # 9
print(roman_to_int("III")) # 3
print(roman_to_int("LVIII")) # 58
print(roman_to_int("MCMXCIV")) # 1994