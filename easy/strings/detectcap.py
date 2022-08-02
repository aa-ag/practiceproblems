def dcu(word: str) -> bool:
    if word == word.title() or word == word.upper() or word == word.lower():
        return True
    return False

# Input: word = "USA"
# Output: true
print(dcu("USA"))

# Input: word = "FlaG"
# Output: false
print(dcu("FlaG"))
