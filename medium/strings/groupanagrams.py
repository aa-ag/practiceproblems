from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = list()

    for i in range(len(strs)):
        print(sorted(strs[i]))


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = [""]
# Output: [[""]]
print(group_anagrams([""]))