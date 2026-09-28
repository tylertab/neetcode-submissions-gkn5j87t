class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.a = []
    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val] = len(self.a)
        self.a.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.a[self.s[val]] = None
            del self.s[val]
            return True
        return False

    def getRandom(self) -> int:
        res = None
        while res == None:
            res = self.a[random.randint(0, len(self.a)- 1)]
        return res


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()