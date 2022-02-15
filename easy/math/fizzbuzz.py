from tracemalloc import start
from typing import List


def fizzBuzz(n: int) -> List[str]:
    return [i for i in range(1, n + 1)]
        

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))