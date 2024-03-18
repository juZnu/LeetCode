from random import choice


class RandomizedSet:

    def __init__(self):
        self.list = {}
        self.all = []

    def insert(self, val: int) -> bool:
        if val not in self.list:
            self.all.append(val)
            self.list[val] = len(self.all)- 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.list:
            ind = self.list[val]
            self.all[ind],self.all[-1] = self.all[-1],self.all[ind]
            self.list[self.all[ind]] = ind
            self.all.pop()
            del self.list[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.all)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()