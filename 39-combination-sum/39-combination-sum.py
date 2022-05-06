class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def helper(index, sumSoFar, slate):
            
            if sumSoFar > target or index >= len(candidates):
                return 
            
            if sumSoFar == target:
                result.append(slate[:])
                return
            
            slate.append(candidates[index])
            helper(index, sumSoFar + candidates[index], slate)
            slate.pop()
            
            helper(index+1, sumSoFar, slate)
        
        helper(0, 0, [])
        return result
            