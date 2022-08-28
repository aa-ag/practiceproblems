from typing import List

def lwc(messages: List[str], senders: List[str]) -> str:
    d = {sender:0 for sender in senders}
    
    for i in range(len(messages)):
        d[ senders[i] ] += len( messages[i].split() )

    if list(d.values()).count(d[max( d, key=d.get )]) == 1:
        return max( d, key=d.get )
    else:
        return max(d.keys())




# Output: "Alice"
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
print(lwc(messages, senders))


# Output: "Charlie"
messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]
print(lwc(messages, senders))