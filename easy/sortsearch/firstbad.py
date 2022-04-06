############------------ FUNCTION(S) ------------############
def first_bad_version(n: int) -> int:
    r = [i for i in range(n-1, -1, -1)]
    return r


############------------ DRIVER CODE ------------############
# Input: n = 5, bad = 4
# Output: 4
print(first_bad_version(5))