class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        previousCalc = nums[0]
        
        for i in range(1, len(nums)):
            previousCalc = max(nums[i], previousCalc + nums[i])
            maxSum = max(previousCalc, maxSum)
            
        
        return maxSum