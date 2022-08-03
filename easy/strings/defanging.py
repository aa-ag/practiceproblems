def defang(address: str) -> str:
    pass



# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
print(defang("1.1.1.1"))

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
print(defang("255.100.50.0"))