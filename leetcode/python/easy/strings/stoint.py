def myAtoi(s):
    '''
     - Read in and ignore any leading whitespace.
     - Check if the next character (if not already at the end of the string) 
        is '-' or '+'. Read this character in if it is either. 
    '''
    low = -(pow(2, 31))
    high = pow(2, 31) -1

    try:
        s = s.lstrip(' ')

        if s.startswith('-'):
            is_negative = True
            s = s.replace('-', '')
        else:
            is_negative = False

        if s.startswith('+'):
            s = s.replace('+', '')
        
        nums = ''

        for i in s:
            if i not in '0123456789':
                break
            else:
                nums += i
        
        try:
            integer = int(nums)

            if is_negative == True:
                integer = int(integer) * -1
                if integer <= low:
                    return low
                return integer

            elif is_negative == False:
                integer = int(integer)
                if integer > high:
                    return high
                return integer
            else:
                return 0
        except:
            return 0
    except:
        return 0


# print(myAtoi("   -42"))
# print(myAtoi("4193 with words"))
# print(myAtoi("words and 987"))
# print(myAtoi("-91283472332"))
print(myAtoi('+-12'))