from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        candidates.sort()
        result: List[List[int]] = []
            
        def helper(index:int, totalSum:int, slate:List[int]):
            
            if totalSum == target:
                result.append(slate[:])
                return
            
            if totalSum > target or index >= len(candidates):
                return 
            
            j = index + 1
            counts = 1
            while j < len(candidates) and candidates[index] == candidates[j]:
                j += 1
                counts += 1
            
            for count in range(0, counts+1):
                partialSum = 0 
                for _ in range(count):
                    partialSum += candidates[index]
                    slate.append(candidates[index])
                helper(index+counts, totalSum + partialSum, slate)
                for _ in range(count):
                    slate.pop()
            
        helper(0,0,[])
        return result
        

        