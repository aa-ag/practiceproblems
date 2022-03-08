# TODO: check 
# https://www.enjoyalgorithms.com/blog/longest-substring-without-repeating-characters

def lengthOfLongestSubstring(s: str) -> int:
    if all(i == s[0] for i in s):
        return 1
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