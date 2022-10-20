class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        maxLength = 0
        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                maxLength = max(maxLength, len(stack))
                stack.pop()
                
        return maxLength
            
        
            