import random


class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return set(random.sample(self.set, 1))

obj = RandomizedSet()
obj.insert(1)
obj.insert(2)
obj.insert(1)
obj.insert(3)
obj.getRandom()