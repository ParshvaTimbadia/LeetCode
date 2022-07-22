class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #First we will sort the array
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums)-1
            
            
            while j < k:
                totalSum = nums[i] + nums[j] + nums[k]
                
                if totalSum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                        
                elif totalSum < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
                    