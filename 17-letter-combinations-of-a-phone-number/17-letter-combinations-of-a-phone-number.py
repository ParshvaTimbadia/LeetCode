from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
    
        store = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        result: List[string] = []
        def helper(index:int, slate:list) -> None:
            
            if len(slate) == len(digits):
                result.append("".join(slate[:]))
                return
            
            for char in store[digits[index]]:
                
                slate.append(char)
                helper(index+1, slate)
                slate.pop()
        
        helper(0, [])
        return result
    
        """
        TimeComplexity: O(n*4^n) 4^n for letters occupied by 7 and 9. N for copying the elements.
        
        SpaceComplexity: O(N) for the call stack.
        
        """
        