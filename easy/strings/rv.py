def rv(s: str) -> str:
    v = list()
    answer = ''

    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            v.append(i)
    return v


# Input: s = "hello"
# Output: "holle"
print(rv("hello"))

# Input: s = "leetcode"
# Output: "leotcede"
print(rv("leetcode"))