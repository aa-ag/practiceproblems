import re

def myAtoi(s):
    '''
     - Read in and ignore any leading whitespace.
     - Check if the next character (if not already at the end of the string) 
        is '-' or '+'. Read this character in if it is either. 
    '''
    low = -(pow(2, 31))
    high = pow(2, 31) -1

    s = s.lstrip(' ')

    if s.startswith('-'):
        is_negative = True
    else:
        is_negative = False

    s = s.replace('-', '')
    
    nums = ''

    for i in s:
        if i not in '0123456789':
            break
        else:
            nums += i
    
    integer = int(nums)
    if is_negative == True and integer >= low:
        return int(nums) * -1
    elif is_negative == False and integer <= high:
        return int(nums)
    else:
        return 0


# print(myAtoi("   -42"))
# print(myAtoi("4193 with words"))
print(myAtoi("words and 987"))