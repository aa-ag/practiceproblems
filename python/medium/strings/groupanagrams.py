from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    d = dict()

    for str in strs:
        k = ''.join(sorted(str))
        if k not in d:
            d[k] = [str]
        else:
            d[k].append(str)
    return d.values()

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = [""]
# Output: [[""]]
print(group_anagrams([""]))