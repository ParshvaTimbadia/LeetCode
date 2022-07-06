class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)-2):
                
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                a = j + 1
                b = len(nums) - 1
                
                while a < b:
                    
                    totalSum = nums[i] + nums[j] + nums[a] + nums[b]
                    
                    if totalSum == target:
                        result.append([nums[i] , nums[j] , nums[a] , nums[b]])
                        a += 1
                        while a < b and nums[a] == nums[a-1]:
                            a += 1
                    elif totalSum < target:
                        a += 1
                    else:
                        b -= 1
        
        return result
                        