class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result: List[str] = []
        def helper(openBracket:int, closeBracket:int, slate: List[str]):
            
            #Backtracking Case:
            if openBracket < closeBracket or openBracket > n or closeBracket > n:
                return
            
            if openBracket == n and openBracket == closeBracket:
                result.append("".join(slate[:]))
                return 
            
            
            slate.append("(")
            helper(openBracket+1, closeBracket, slate)
            slate.pop()
            
            slate.append(")")
            helper(openBracket, closeBracket+1, slate)
            slate.pop()
        
        helper(0, 0, [])
        return result
            
            