############------------ IMPORTS ------------############


############------------ FUNCTION(S) ------------############
def get_sum(a: int, b: int) -> int:
    '''
     Given two integers a and b, 
     return the sum of the two integers 
     without using the operators + and -
    '''
    ### version from geeksforgeeks
    while b != 0:
        carry = a & b

        a = a ^ b

        b = carry << 1

    return a


############------------ DRIVER CODE ------------############
'''
Input: a = 1, b = 2
Output: 3
'''
a = 1
b = 2
print(get_sum(a, b))

'''
Input: a = 2, b = 3
Output: 5
'''
a = 2
b = 3
print(get_sum(a, b))

