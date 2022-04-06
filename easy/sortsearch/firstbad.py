############------------ FUNCTION(S) ------------############
def first_bad_version(n: int) -> int:
    return [i for i in range(1, n)]


############------------ DRIVER CODE ------------############
# Input: n = 5, bad = 4
# Output: 4
print(first_bad_version(5))