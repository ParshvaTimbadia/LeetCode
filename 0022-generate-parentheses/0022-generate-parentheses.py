class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        result = []
        def helper(start, close, slate):
            
            if start < close:
                return
            
            if start > n or close > n:
                return
            
            if start == close and close == n:
                result.append("".join(slate[:]))
                return
            
            slate.append("(")
            helper(start + 1, close, slate)
            slate.pop()
            
            slate.append(")")
            helper(start, close + 1, slate)
            slate.pop()
        
        helper(0,0,[])
        return result
            
                