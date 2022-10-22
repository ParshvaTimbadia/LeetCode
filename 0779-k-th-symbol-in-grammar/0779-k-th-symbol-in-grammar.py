import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0 
        # 0 1
        # 0 1 1 0
        # 0 1 1 0 1 0 0 1
        
        def helper(n, k):
            if n == 1:
                return 0
                
            parent = helper(n-1, math.ceil(k/2))
              
            isKOdd = k % 2 == 1
            
            if parent == 1:
                return 1 if isKOdd else 0
            else:
                return 0 if isKOdd else 1
        
        return helper(n, k)
                
        