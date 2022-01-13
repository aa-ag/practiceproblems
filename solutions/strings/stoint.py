def myAtoi(s):
    '''
     - Read in and ignore any leading whitespace.
     - Check if the next character (if not already at the end of the string) 
        is '-' or '+'. Read this character in if it is either. 
    '''
    s = s.lstrip(' ')
    if s.startswith('-'):
        print("negative")
    else:
        print("positive")

myAtoi("   -42")