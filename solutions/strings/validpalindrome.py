def isPalindrome(s):
    '''
        (1) remove all non-alphanumeric characters
        (2) check if s == s.reversed()
        (3) if s is a white space, return true
    '''
    if set(s) == ' ':
        return True

    import re
    clean = re.sub('[^a-zA-Z0-9]|\_', '', s.lower())
    print(clean)
    return clean == clean[::-1]

print(isPalindrome("A man, a plan, a canal: Panama"))
# print(isPalindrome("race a car"))
# print(isPalindrome(" "))
print(isPalindrome("ab_a"))