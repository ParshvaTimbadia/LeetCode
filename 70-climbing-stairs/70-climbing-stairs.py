class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        if n == 1:
            return 1
        
        result = [1]*(n + 1)
        
        for i in range(2, n + 1):
            result[i] = result[i-1] + result[i-2]
        
        return result[-1]