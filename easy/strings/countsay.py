nums = {
    '1': 'one','2': 'two','3': 'three','4': 'four','5': 'five',
    '6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'ten',
}

def countAndSay(n: int) -> str:
    # a_value = nums[n]
    # a_key = list(nums.keys())[list(nums.values()).index(nums[n])]
    
    i = 1
    count = ''
    say = ''
    while i < n + 1:
        count = str(i)
        print(count)
        
        say = f"{nums[count]} {count}" 
        print(say)

        new_count = list(nums.keys())[list(nums.values()).index(nums[count])]
        new_say = count + new_count
        print(new_say)

        i += 1
        break

# Input: n = 4
# Output: "1211"
countAndSay(4)
# print(countAndSay(4))