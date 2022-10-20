class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def helper(n, k):
            if n == 1:
                return 0
            x = helper(n-1, k)
            y = (x + k) % n
            return y
        
        return helper(n, k) + 1
        
    
        # TimeComplexity: O(N**2)
        # Space Complexity: Since we are using the queue of size N, it would be O(N).