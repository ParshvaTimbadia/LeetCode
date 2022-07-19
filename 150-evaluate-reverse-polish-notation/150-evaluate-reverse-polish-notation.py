class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        symbol = set(["+", "-", "*", "/"])
        
        for item in tokens:
            if stack and item in symbol:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                
                if item == "+":
                    stack.append(num1 + num2)
                elif item == "-":
                    stack.append(num2 - num1)
                elif item == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(int(num2/num1))
            else:
                stack.append(int(item))
        
        return stack[-1]
                
                