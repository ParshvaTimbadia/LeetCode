class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        result = []
        def helper(index,sumSoFar, slate):
            
            #Backtracking Case
            if sumSoFar > target or index == len(candidates):
                return
            
            #BaseCondition
            if target == sumSoFar:
                result.append(slate[:])
                return
            
                        
            #Exclude
            helper(index+1, sumSoFar, slate)
            
            #include
            slate.append(candidates[index])
            helper(index, sumSoFar + candidates[index], slate)
            slate.pop()
            
        
        helper(0, 0, [])
        return result
            
            