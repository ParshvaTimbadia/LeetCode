class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if len(nums)==0:
            return []
        
        
        nums.sort()
        dp = [[num] for num in nums]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
        
        return max(dp, key = lambda x:len(x))