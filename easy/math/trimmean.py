from typing import List

def tm(arr: List[int]) -> float:
    l = len(arr)
    five_percent = int(l * 0.05)
    arr.sort()
    arr =  arr[five_percent:-five_percent]
    mean = round(sum(arr) / len(arr), 5)
    return mean

# Input: arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
# Output: 2.00000
print(tm([1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]))

# Input: arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
# Output: 4.00000
print(tm([6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]))

# Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# Output: 4.77778
print(tm([6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]))
