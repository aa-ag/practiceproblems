from collections import Counter

nums = {
    '1': 'one','2': 'two','3': 'three','4': 'four','5': 'five',
    '6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'ten',
}

def countAndSay(n: int) -> str:    
    i = 1
    count = str(i)
    say = ''
    while i < n:
        print(f"--->{i}")
        print(count)
        
        current_count = Counter(count)
        print(current_count)

        for k, v in current_count.items():
            say = f"{nums[str(v)]} {k}" 
            print(say)

        count = count + list(nums.keys())[list(nums.values()).index(nums[str(v)])]
        print(count)

        i += 1

    return count

# Input: n = 4
# Output: "1211"
# countAndSay(4)
print(countAndSay(4))