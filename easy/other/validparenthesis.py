

def is_valid(s: str) -> bool:
    '''
     create an empty list to use as a stack,
     add to stack when opening parenthesis is found,
     pop from the stack when closing parenthesis is found
    '''
    stack = list()

    for i in s:
        if i in ['(', '[', '\{']:
            stack.append(i)
        elif i in [')', ']', '\}']:
            stack.pop()

    return not len(stack)



print(is_valid("()[]\{\}"))

print(is_valid("(]"))

print(is_valid("{ { ( { } ) } }"))