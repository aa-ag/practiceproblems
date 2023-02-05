class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
         O(nlogn) time: sorting costs + comparing sorted strings
         O(1) space: Space depends on the sorting implementation which, usually, 
          costs O(1)O(1) auxiliary space if heapsort is used
        '''
        return sorted(s) == sorted(t)