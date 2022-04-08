class Solution:
    def numTrees(self, n: int) -> int:
        
        #Memoization
        seen = {1:1, 0:1, 2:2}
        
        def helper(n):
            
            if n in seen:
                return seen[n]
            
            result = 0
            for i in range(1,n+1):
                result += helper(i-1) * helper(n-i)
            
            seen[n] = result
            return seen[n]
        
        return helper(n)