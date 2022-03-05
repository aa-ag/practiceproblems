

def is_valid(s: str) -> bool:
    '''
     need to rethink this one
    '''
    while '()' in s or '\{\}' in s or '[]' in s:
        s = s.replace('()', '').replace('\{\}', '').replace('[]', '')
    if s == '':
        return True
    return False

# True
print(is_valid("()"))

# True
print(is_valid("()[]\{\}"))

# False
print(is_valid("(]"))

# print(is_valid("{ { ( { } ) } }"))