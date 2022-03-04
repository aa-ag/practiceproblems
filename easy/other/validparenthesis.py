

def is_valid(s: str) -> bool:
    stack = list()

    for i in s:
        if i in ['(', '[', '\{']:
            stack.append(i)
        elif i in [')', ']', '\}']:
            stack.pop()

    return stack



print(is_valid("()[]\{\}"))

print(is_valid("(]"))

print(is_valid("{ { ( { } ) } }"))