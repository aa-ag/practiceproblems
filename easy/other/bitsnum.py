# get number of '1' bits on an unsigned integer

def hamming_weight(n: int) -> int:
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count


# Input: n = 00000000000000000000000000001011
# Output: 3
print(hamming_weight('00000000000000000000000000001011'))

# Input: n = 00000000000000000000000010000000
# Output: 1
print(hamming_weight('00000000000000000000000010000000'))

# Input: n = 11111111111111111111111111111101
# Output: 31
print(hamming_weight('11111111111111111111111111111101'))