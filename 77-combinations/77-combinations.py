from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        result:List[List[int]] = []
        def helper(num:int, slate:List[int]) -> None:
            
            #Backtracking case
            
            if len(slate) == k:
                result.append(slate[:])
                return
            
            if num > n:
                return
            
            #Include
            slate.append(num)
            helper(num+1, slate)
            slate.pop()
            
            #Exclude
            helper(num+1,slate)
        
        helper(1,[])
        return result
            