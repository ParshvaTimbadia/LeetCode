class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]
        
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for c in range(amount + 1):
            if coins[0] <= c:
                dp[0][c] = dp[0][c - coins[0]]
    
        
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                
                dp[i][j] = dp[i-1][j]
                
                if coins[i] <= j:
                    dp[i][j] += dp[i][j - coins[i]]
        
        
        return dp[-1][-1]