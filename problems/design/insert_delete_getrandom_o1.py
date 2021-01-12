import random
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.list = []
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.set:
            return False
        else:
            self.set.add(val)
            self.list.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.set:
            self.set.remove(val)
            self.list.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.list) == 0:
            return
        idx = random.randint(0, len(self.list) - 1)
        return random.choice(self.list)

if __name__ == '__main__':
    obj = RandomizedSet()
    print(obj.insert(1))
    print(obj.insert(2))
    # print(obj.remove(1))
    print(obj.getRandom())