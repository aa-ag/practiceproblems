def rv(s: str) -> str:
    v = list()
    answer = ''

    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            v.append(i)
    
    for j in v:
        s[j] = v[-1]
        v = v[:-1]
    
    print(s)


# Input: s = "hello"
# Output: "holle"
print(rv("hello"))

# Input: s = "leetcode"
# Output: "leotcede"
print(rv("leetcode"))