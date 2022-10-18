class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        
        prefix_sum = 0
        totalSum = sum(nums)
        
        for i in range(len(nums)):
            if totalSum - nums[i] - prefix_sum == prefix_sum:
                return i
            prefix_sum += nums[i]
        
        return -1