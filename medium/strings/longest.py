import re

def lengthOfLongestSubstring(s: str) -> int:
    if all(i == s[0] for i in s):
        return 1

    temp = ''

    for i in s:
        if i not in temp:
            temp += i
        else:
            continue
    
    if temp in s:
        return len(temp)
    



# Input: s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring("abcabcbb"))


# Input: s = "bbbbb"
# Output: 1
print(lengthOfLongestSubstring("bbbbb"))


# Input: s = "pwwkew"
# Output: 3
print(lengthOfLongestSubstring("pwwkew"))