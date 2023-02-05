from typing import List


def count_primes(n: int) -> int:
    '''
     Sieve of Eratosthenes
    '''
    array = [True] * n
    
    count = 0
    for i in range(2,n):
        if array[i]:
            count += 1
        if not array[i]: 
            continue
            
        for j in range(i+i, n, i):
            array[j] = False
        
    return count


print(count_primes(0))
print(count_primes(1))
print(count_primes(10))

