class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        dp = [False]*len(nums)
        dp[0] = True
        
        
        for i in range(1, len(nums)):
            
            j = i - 1
            possible = False
            while j >= 0:
                if j + nums[j] >= i and dp[j] == True:
                    possible = True
                    break
                j -= 1
            
            dp[i] = possible
        
        return dp[-1]
            
            
                