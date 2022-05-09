class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        def helper(index, slate):
            
            if index >= len(nums):
                result.append(slate[:])
                return
            
            counts = 1
            i = index + 1
            while (i < len(nums) and nums[i] == nums[i-1]):
                counts+=1
                i+=1
            
            for count in range(0, counts+1):
                
                for _ in range(count):
                    slate.append(nums[index])
                
                helper(index+counts,slate)
                
                for _ in range(count):
                    slate.pop()
        
        helper(0, [])
        return result
            
            
            
        