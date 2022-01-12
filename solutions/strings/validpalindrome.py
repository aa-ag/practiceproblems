def isPalindrome(s):
    '''
        (1) remove all non-alphanumeric characters
        (2) check if s == s.reversed()
        (3) if s is a white space, return true
    '''
    if set(s) == ' ':
        return True

    import re
    clean = re.sub('\W', '', s.lower())
    print(clean)

isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")
isPalindrome(" ")