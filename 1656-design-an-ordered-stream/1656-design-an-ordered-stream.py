class OrderedStream:

    def __init__(self, n: int):
        self.array = [None]*(n + 1) 
        self.pointer = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.array[idKey] = value
        result = []
        while self.pointer < len(self.array) and self.array[self.pointer]:
            result.append(self.array[self.pointer])
            self.pointer += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)