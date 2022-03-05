from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        # Partial Soltion: slate
        # Subproblem Definition: index
        result: List[int] = []
        def helper(index:int, slate: List) -> None:
            
            if index == len(nums):
                result.append(slate[:])
                return
            
            #Two cases -> Either include or exclude
            helper(index+1, slate)
            
            slate.append(nums[index])
            helper(index+1, slate)
            slate.pop()
        
        helper(0, [])
        return result
    
        """
        TimeComplexity: Every position will have 2 possibilities to either include or exclude. O(2^n)
        Copying the slate to the result will take O(n).
        Overall : O(n*2^n)
        
        
        Space Complexity: O(n*2^n)
        """