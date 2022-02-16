from typing import List


def count_primes(n: int) -> int:
    dp = [True] * n
    
    count = 0
    for i in range(2,n):
        if dp[i]:
            count += 1
        if not dp[i]: 
            continue
            
        for j in range(i+i, n, i):
            dp[j] = False
        
    return count


print(count_primes(0))
print(count_primes(1))
print(count_primes(10))

