class MyStack:
    def __init__(self):
        self.stack = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
        