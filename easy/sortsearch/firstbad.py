############------------ FUNCTION(S) ------------############
def first_bad_version(n: int) -> int:
    left, right = 1, n

    while left <= right:
        mid = (left+right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


############------------ DRIVER CODE ------------############
# Input: n = 5, bad = 4
# Output: 4
print(first_bad_version(5))