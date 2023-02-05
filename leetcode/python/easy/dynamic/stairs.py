
def climb_stairs(n: int) -> int:
    stairs = [0] * (n + 2)
    stairs[1] = 1
    stairs[2] = 2

    
    for i in range(3, len(stairs)):
        stairs[i] = stairs[i - 1] + stairs[i - 2]
    
    return stairs[n]


# def climb_stairs(n: int) -> int:
#     if n == 1 or n == 2:
#         return n
#     else:
#         first_step = 1
#         second_step = 2
#         for step in range(3, n+1):
#             x = first_step + second_step
#             first_step = second_step
#             second_step = x
#         return x



print(climb_stairs(2))

print(climb_stairs(3))