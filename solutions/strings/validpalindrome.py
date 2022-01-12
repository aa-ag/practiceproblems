def isPalindrome(self, s: str) -> bool:
    '''
        (1) remove all non-alphanumeric characters
        (2) check if s == s.reversed()
        (3) if s is a white space, return true
    '''
    import re
    clean = re.sub('W+', '', s)
    print(clean)

isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")
isPalindrome(" ")