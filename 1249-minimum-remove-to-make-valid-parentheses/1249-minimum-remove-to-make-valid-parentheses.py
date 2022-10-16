class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        for index, char in enumerate(s):
            if char == ")" and stack and stack[-1][0] == "(":
                stack.pop()
            elif char == "(" or char == ")":
                stack.append([char, index])
        
        remove = set([item[1] for item in stack])
        
        result = []
        for index, char in enumerate(s):
            if index in remove:
                continue
            result.append(char)
        
        return "".join(result)
                
                
            