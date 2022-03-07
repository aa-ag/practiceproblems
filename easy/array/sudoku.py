from typing import List
# import numpy as np

# TODO: check this out: 
# https://www.youtube.com/watch?v=ClvYxCvzpEQ


def is_valid(board: List[List[str]]) -> bool:
    # for row in board:
    #     nums = [int(i) for i in row if i != '.']
    #     for n in nums:
    #         if n > 9 or n < 0 or nums.count(n) > 1:
    #             return False
    #     print(row)
    three_by_three = list()

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = board[i][j:j+3] + \
                board[i+1][j:j+3] + \
                    board[i+2][j:j+3]
            three_by_three.append(block)
        
    print(three_by_three)


board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
# Output: true
# print(is_valid(board))
is_valid(board)


board = [
    ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
# Output: false
# print(is_valid(board))

