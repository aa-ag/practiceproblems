from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagrams = set()

    for str in strs:
        anagrams.add(''.join(sorted(str)))

    d = dict()

    for anagram in list(anagrams):
        d[anagram] = list()

    print(d)
            


# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

# Input: strs = [""]
# Output: [[""]]
# print(group_anagrams([""]))