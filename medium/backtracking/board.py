from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    pass


board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# Input: word = "ABCCED"
# Output: true
print(exist(board, "ABCCED"))

# Input: word = "SEE"
# Output: true
print(exist(board, "SEE"))

# Input: word = "ABCB"
# Output: false
print(exist(board, "ABCB"))