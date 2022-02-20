class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        pass


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = 1
obj.push(val)
val = 2
obj.push(val)
print(obj.stack)
obj.pop()
print(obj.stack)
param_3 = obj.top()
print(param_3)
# param_4 = obj.getMin()