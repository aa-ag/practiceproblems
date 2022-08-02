def dcu(word: str) -> bool:
    if word == word.title():
        return True
    elif word == word.upper():
        return True
    elif word == word.lower():
        return True
    else:
        return False

# Input: word = "USA"
# Output: true
print(dcu("USA"))

# Input: word = "FlaG"
# Output: false
print(dcu("FlaG"))
