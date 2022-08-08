class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        dp = [[math.inf for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for i in range(len(coins)):
            dp[i][0] = 0
            
        for i in range(len(coins)):
            for c in range(1, amount + 1):
                
                if i > 0:
                    dp[i][c] = dp[i-1][c]
                if coins[i] <= c:
                    if dp[i][c - coins[i]] != math.inf:
                        dp[i][c] = min(dp[i][c], dp[i][c - coins[i]] + 1)
        
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1
                