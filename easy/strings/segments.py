def countSegments(s: str) -> int:
    return len(s.split())


# Input: s = "Hello, my name is John"
# Output: 5
print(countSegments("Hello, my name is John"))

# Input: s = "Hello"
# Output: 1
print(countSegments("Hello"))