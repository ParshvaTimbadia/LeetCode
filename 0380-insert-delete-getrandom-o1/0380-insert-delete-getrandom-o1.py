class RandomizedSet:

    def __init__(self):
        self.set = collections.defaultdict(int)
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        self.set[val] = len(self.arr)
        self.arr.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        indexToRemove = self.set[val]
        self.arr[indexToRemove], self.arr[-1] = self.arr[-1], self.arr[indexToRemove]
        self.set[self.arr[indexToRemove]] = indexToRemove
        del self.set[self.arr[-1]]
        self.arr.pop()
        return True
        

    def getRandom(self) -> int:
        #Get random is called on an array list.
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()