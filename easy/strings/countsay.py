nums = {
    '1': 'one','2': 'two','3': 'three','4': 'four','5': 'five',
    '6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'ten',
}

def countAndSay(n: int) -> str:
    a_value = nums[n]
    a_key = list(nums.keys())[list(nums.values()).index(nums[n])]
    
    for i in range(1, n + 1):
        print(i)

# Input: n = 4
# Output: "1211"
countAndSay(4)
# print(countAndSay(4))