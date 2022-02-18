from typing import List


def max_profit(prices: List[int]) -> int:

    profit = 0

    for i in range(1, len(prices)):
        if prices[i-1] < prices[i]:
            move = prices[i] - prices[i-1]
            profit += move

    return profit


# expects 3
print(max_profit([1,2,4]))

# Input: prices = [7,1,5,3,6,4]
# Output: 7
print(max_profit([7,1,5,3,6,4]))

# Input: prices = [1,2,3,4,5]
# Output: 4
print(max_profit([1,2,3,4,5]))

# Input: prices = [7,6,4,3,1]
# Output: 0
print(max_profit([7,6,4,3,1]))