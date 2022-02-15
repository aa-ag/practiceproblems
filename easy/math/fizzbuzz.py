from tracemalloc import start
from typing import List


def fizzBuzz(n: int) -> List[str]:
    answer = list()

    for i in range(1, n + 1):
        current = ""
        if i % 3 == 0:
            current += "Fizz"
        if i % 5 == 0:
            current += "Buzz"
        if i % 5 != 0 and i % 3 != 0:
            current = str(i)
        
        answer.append(current)
    return answer
        
        
print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))