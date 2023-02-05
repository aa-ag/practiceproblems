import random


class RandomizedSet:
    def __init__(self):
        self.set = list()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.set)

obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(1)
obj.insert(3)
print(obj.getRandom())