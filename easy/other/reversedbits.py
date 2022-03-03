

def reverse_bits(self, n: int) -> int:
    '''
     one step at the time version
    '''
    b = bin(n)[:2]
    reveresed_b = b[::-1]
    return int(reveresed_b, 2)


# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
print(reverse_bits('00000010100101000001111010011100'))


# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
print(reverse_bits('11111111111111111111111111111101'))