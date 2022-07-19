class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = math.inf
        

    def push(self, val: int) -> None:
        self.minimum = min(val, self.minimum)
        self.stack.append((val, self.minimum))
        

    def pop(self) -> None:
        if self.stack:
            data = self.stack.pop()
        
        if len(self.stack) == 0:
            self.minimum = math.inf
        else:
            self.minimum = self.stack[-1][1]
        

    def top(self) -> int:
        return self.stack[-1][0] 

    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()