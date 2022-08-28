from typing import List

def lwc(messages: List[str], senders: List[str]) -> str:
    d = {sender:0 for sender in senders}
    
    for i in range(len(messages)):
        d[ senders[i] ] += len( messages[i].split() )

    maximun = d[ max(d, key=d.get) ]
    
    answer = ''

    for k, v in d.items():
        if v == maximun and answer < k:
            answer = k
    
    return answer




# Output: "Alice"
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
print(lwc(messages, senders))


# Output: "Charlie"
messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]
print(lwc(messages, senders))