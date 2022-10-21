class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        def helper(index, slate, totalSum):
            
            #Base case
            if index == len(candidates) or totalSum > target:
                return
            
            if totalSum == target:
                result.append(slate[:])  
                return
                
            #Include
            slate.append(candidates[index])
            helper(index, slate, totalSum + candidates[index])
            slate.pop()
            
            #exlcude
            helper(index + 1, slate, totalSum)
        
        helper(0, [], 0)
        return result