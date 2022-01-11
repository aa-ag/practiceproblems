class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''
         O(n) time
         O(1) space
        '''
        import collections
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
