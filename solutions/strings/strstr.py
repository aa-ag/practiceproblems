import re

def strStr(h: str, n: str) -> int:
    if n == "":
        return 0
    
    try:
        return re.search(n, h).start()
    except:
        return -1


# Input: haystack = "hello", 
# needle = "ll"
# Output: 2
print(strStr("hello", "ll"))

# Input: haystack = "aaaaa", 
# needle = "bba"
# Output: -1
print(strStr("aaaaa", "bba"))

# Input: haystack = "", 
# needle = ""
# Output: 0
print(strStr("", ""))
