class MinStack:

    def __init__(self):
        self.stack = list()
        self.minimums = list()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = 100
obj.push(val)
val = 20
obj.push(val)
val = 25
obj.push(val)
val = 3
obj.push(val)
print(obj.stack)
obj.pop()
print(obj.stack)
param_3 = obj.top()
print(param_3)
param_4 = obj.get_min()
print(param_4)