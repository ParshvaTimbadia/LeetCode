class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            start = i + 1
            end = len(nums) - 1
            
            while start < end:
                
                totalSum = nums[i] + nums[start] + nums[end]
                
                if totalSum == 0:
                    result.append([nums[i] , nums[start] , nums[end]])
                    
                    start += 1
                    end -= 1
                    
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    
                elif totalSum < 0:
                    start += 1
                else:
                    end -= 1
        
        return result
                
                
                