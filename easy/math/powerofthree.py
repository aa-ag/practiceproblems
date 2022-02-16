def is_power_of_three(n: int) -> bool:
    '''
     O(1) time complexity: only one operation takes place
     O(1) space complexity: no additional memory is used
    '''
    return n > 0 and 1162261467 % n == 0


# def is_power_of_three(n: int) -> bool:
#     '''
#      O(log3(n)) time complexity: where 3 is the number of divisions
#      O(1) space complexity: no additional space required
#     '''
#     if n < 1:
#         return False

#     while n % 3 == 0:
#         n /= 3

#     return n == 1


print(is_power_of_three(27))

print(is_power_of_three(0))

print(is_power_of_three(9))

print(is_power_of_three(45))