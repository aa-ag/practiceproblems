def reformat(number: str) -> str:
    digits = ''.join(i for i in number if i.isdigit())

    answer = ''

    while len(digits) > 4:
        chunk = digits[:3]
        answer += chunk + '-'
        digits = digits[3:]

    if len(digits) in (2, 3):
        answer += digits
    else:
        answer += f"{digits[:2]}-{digits[2:]}"
    return answer


# Input: number = "1-23-45 6"
# Output: "123-456"
print(reformat("1-23-45 6"))

# Input: number = "123 4-567"
# Output: "123-45-67"
print(reformat("123 4-567"))

# Input: number = "123 4-5678"
# Output: "123-456-78
print(reformat("123 4-5678"))