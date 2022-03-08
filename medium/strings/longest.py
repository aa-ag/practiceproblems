

def lengthOfLongestSubstring(s: str) -> int:
    answer = ''

    for i in s:
        if i not in answer:
            answer += i
        else:
            return len(answer)



# Input: s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring("abcabcbb"))


# Input: s = "bbbbb"
# Output: 1
print(lengthOfLongestSubstring("bbbbb"))


# Input: s = "pwwkew"
# Output: 3
print(lengthOfLongestSubstring("pwwkew"))