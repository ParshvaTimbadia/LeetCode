class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        # SubProblem Definition x**10 = X**5 x X**5 for even powers and for odd x*X**5 x X**5
        # Partial Solution 
        
        def helper(x, n):
            
            if n == 1:
                return x
            
            if n == 0:
                return 1
            
            sub_problem = helper(x, n//2)
            if n%2 == 0:
                return sub_problem*sub_problem
            else:
                return x*sub_problem*sub_problem
        
        if n > 0:
            return helper(x, n)
        else:
            return 1/helper(x, abs(n))
    