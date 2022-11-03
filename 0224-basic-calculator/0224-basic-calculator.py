class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        ans = 0
        sign = 1 # 1 denotes positive and -1 denotes negative.
        i = 0
        while i < len(s):
            
            if s[i].isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number*10 + int(s[i])
                    i += 1
                i-=1
                ans += sign*number
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif s[i] == ")":
                ans = stack.pop()*ans
                ans += stack.pop()
            
            i += 1
        
        return ans
                
                
        