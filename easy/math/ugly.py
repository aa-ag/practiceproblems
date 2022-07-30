from sympy.ntheory import primefactors

def is_ugly(n: int) -> bool:
    pf = primefactors(n)
    print(pf)
    return pf == [2,3,5] or pf == []


# Input: n = 6
# Output: true
print(is_ugly(6))

# Input: n = 1
# Output: true
print(is_ugly(1))

# Input: n = 14
# Output: false
print(is_ugly(14))