from typing import List

def lwc(messages: List[str], senders: List[str]) -> str:
    pass


# Output: "Alice"
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["Alice","userTwo","userThree","Alice"]
print(lwc(messages, senders))


# Output: "Charlie"
messages = ["How is leetcode for everyone","Leetcode is useful for practice"]
senders = ["Bob","Charlie"]
print(lwc(messages, senders))