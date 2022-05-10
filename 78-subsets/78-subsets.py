class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def helper(index,slate):
            
            #Base Condition:
            if index == len(nums):
                result.append(slate[:])
                return
            
            #Exclude
            helper(index+1, slate)
            
            #Include
            
            #Do
            slate.append(nums[index])
            helper(index+1, slate)
            #Undo
            slate.pop()
        
        helper(0, [])
        return result
            
        """
        
        
        
        
        
        """