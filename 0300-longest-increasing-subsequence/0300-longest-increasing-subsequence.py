class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
    
        dp = [1]*len(nums)
        maxLength = 1
        
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            maxLength = max(maxLength, dp[i])
        
        return maxLength