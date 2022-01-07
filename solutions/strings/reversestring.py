class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
         Do not return anything, modify s in-place instead.
        """
        ### Python's reverse() reverses the elements of a list in place
        ### this means O(n) Time Complexity
        # s.reverse()
        ### another version would be
        ### while time remains O(n), space complexity = O(1)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
