class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        for index, char in enumerate(s):
            if stack and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            
            if stack[-1][1] == k:
                stack.pop()
         
        result = []
        for st in stack:
            result.append(st[0]*st[1])
        
        return "".join(result)
    