from typing import List


def count_primes(n: int) -> int:
    count = 0

    for i in range(n):
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count += 1
    return count


print(count_primes(0))
print(count_primes(1))
print(count_primes(10))

