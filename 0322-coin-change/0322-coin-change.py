class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
        func(i, amount) = 1  + min(func(i, amount - coin[i]), func(i+1, amount))        
        """
        
        dp = [[math.inf for _ in range(amount+1)] for _ in range(len(coins))]
        
        for i in range(len(coins)):
            dp[i][0] = 0
        
        for i in range(1, amount+1):
            if coins[0] <= i:
                dp[0][i] = 1 + dp[0][i-coins[0]]
              
        
        for r in range(1, len(coins)):
            for c in range(1, amount + 1):
                if coins[r] <= c:
                    if dp[r][c - coins[r]] != math.inf:
                        dp[r][c] = dp[r][c - coins[r]] + 1
                
                dp[r][c] = min(dp[r][c], dp[r-1][c])
        
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1
                    