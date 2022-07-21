class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def calculate(s):
            
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            
            return stack
        
        return calculate(s) == calculate(t)