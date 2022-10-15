class Solution:
    def knightDialer(self, n: int) -> int:
        
        
        numberMap = {1:[6,8],2:[7,9],3:[4,8],4:[3,0,9],5:[],6:[1,7,0],7:[2,6],8:[1,3],9:[2,4],0:[4,6]}
        
        dp = [1]*10
        
        for i in range(2, n+1):
            
            old_dp = dp.copy()
            
            for j in range(10):
                
                dp[j] = 0
                
                for num in numberMap[j]:
                
                    dp[j] += old_dp[num]
        
        return sum(dp)%(10**9 + 7)
                