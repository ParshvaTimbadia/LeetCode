class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            if n == 1:
                return x
            if n <= 0:
                return 1
            
            result = helper(x, n//2)
            
            if n%2 == 0:
                return result*result
            
            return x*result*result
        
        if n < 0:
            return 1/helper(x, abs(n))
        return helper(x, n)