def is_valid(s: str) -> bool:
    stack = []
    open_set = set(['(', '[', '{'])
    open_to_close = {'(' : ')', '{' : '}', '[' : ']'}
    
    for parenthesis in s:
        if parenthesis in open_set:
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False
            
            open_p = stack.pop()
            if parenthesis != open_to_close[open_p]:
                return False
            
    return not stack


# def is_valid(s: str) -> bool:
#     '''
#      need to rethink this one
#     '''
#     while '()' in s or '\{\}' in s or '[]' in s:
#         s = s.replace('\{\}', '').replace('()', '').replace('[]', '')
#     if s == '':
#         return True
#     return False

# True
print(is_valid("()"))

# True
print(is_valid("()[]\{\}"))

# False
print(is_valid("(]"))

print(is_valid("{ { ( { } ) } }"))