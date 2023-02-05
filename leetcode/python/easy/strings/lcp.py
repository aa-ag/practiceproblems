import os.path as p

def longestCommonPrefix(strs: list) -> str:
    return p.commonprefix(strs)
        


strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))

strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))