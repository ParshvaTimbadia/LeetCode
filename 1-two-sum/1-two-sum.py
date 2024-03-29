class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        
        i = 0 
        j = len(nums)-1
        
        while i < j:
            if nums[i][0] + nums[j][0] == target:
                return [nums[i][1] ,nums[j][1]]
            elif nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                j -= 1
        
        