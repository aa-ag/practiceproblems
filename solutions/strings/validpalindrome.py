class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
         (1) remove all non-alphanumeric characters
         (2) check if s == s.reversed()
         (3) if s is a white space, return true
        '''