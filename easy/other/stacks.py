class MyStack:
    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        top = self.stack[-1]
        self.stack = self.stack[:-1]
        return top