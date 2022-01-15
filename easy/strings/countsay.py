############------------ IMPORTS ------------############
from collections import Counter
from lib2to3.pgen2 import driver


############------------ GLOBAL VARIABLE(S) ------------############
nums = {
    '1': 'one','2': 'two','3': 'three','4': 'four','5': 'five',
    '6': 'six','7': 'seven','8': 'eight','9': 'nine','0': 'ten',
}


############------------ FUNCTION(S) ------------############
def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    # set i to 1 since we expect to 
    # have n loops from 1 to n 
    i = 1

    # set count initially to 1
    # as a string to consume nums
    count = str(i)

    # say step will be a string,
    # initially empty
    say = ''

    # n times do the following
    while i < n:
        # print(f"--->{i}")
        # print(count)
        
        # count how many of each digit there is
        current_count = Counter(count)
        # print(current_count)

        # for each of those digits,
        # "say" how many there are
        answer = ''
        for k, v in current_count.items():
            say = f"{nums[str(v)]} {k}" 
            # print(say)

            # update the count to the digit version of 
            # the count + the digit
            count = list(nums.keys())[list(nums.values()).index(nums[str(v)])] + k
            answer += count
            # print(answer)

        # go again
        i += 1

    return answer


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    # Input: n = 4
    # Output: "1211"
    # countAndSay(4)
    print(countAndSay(1))