
def is_power_of_three(n: int) -> bool:
    if n <= 1:
        return False
    return n % 3 == 0


print(is_power_of_three(27))

print(is_power_of_three(0))

print(is_power_of_three(9))

print(is_power_of_three(45))