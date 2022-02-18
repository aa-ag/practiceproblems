from audioop import reverse
from typing import List

def max_profit(prices: List[int]) -> int:
    if prices == sorted(prices, reverse=True):
        return 0


# Input: prices = [7,1,5,3,6,4]
# Output: 7
print(max_profit([7,1,5,3,6,4]))

# Input: prices = [1,2,3,4,5]
# Output: 4
print(max_profit([1,2,3,4,5]))

# Input: prices = [7,6,4,3,1]
# Output: 0
print(max_profit([7,6,4,3,1]))