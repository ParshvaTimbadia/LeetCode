class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        
        """
        [1, 2, 3]
        [1, 3, 2]
        [2, 1, 3]
        [2, 3, 1]
        [3, 2, 1]
        
        """
        
        result: List[int] = []
        def helper(index:int) -> None:
            
            if index == len(nums):
                result.append(nums[:])
                return
            
            for i in range(index, len(nums)):
                
                nums[i], nums[index] = nums[index], nums[i]
                
                helper(index+1)
                
                nums[i], nums[index] = nums[index], nums[i]
        
        helper(0)
        return result
        
        """
        TimeComplexity: O(n*n!)
        
        SpaceComplexity: O(n*n!)
        
        
        """
                