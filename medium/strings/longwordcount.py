from email import message
from typing import List

def lwc(messages: List[str], senders: List[str]) -> str:
    d = dict()

    for sender in senders:
        if sender not in d:
            d[ sender ] = 0
    
    for i in range(len(messages)):
        d[ senders[i] ] += len( messages[i].split() )

    return max( d, key=d.get )



# Output: "Alice"
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
print(lwc(messages, senders))


# Output: "Charlie"
messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]
print(lwc(messages, senders))