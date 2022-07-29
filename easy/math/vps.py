
def vps(num: int) -> bool:
    '''
     check if an integer is a valid perfect square
    '''
    return num ** 0.5 


# Input: num = 16
# Output: true
print(vps(16))

# Input: num = 14
# Output: false
print(vps(14))