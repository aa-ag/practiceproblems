def rv(s: str) -> str:
    v = list()
    answer = ''

    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            v.append(i)
    
    for j in range(len(s)):
        if s[j] in 'aeiouAEIOU':
            answer += s[ v[-1] ]
            v = v[:-1]
        else:
            answer += s[j]

    return answer


# Input: s = "hello"
# Output: "holle"
print(rv("hello"))

# Input: s = "leetcode"
# Output: "leotcede"
print(rv("leetcode"))