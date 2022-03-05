from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        #partial solution : slate
        # subproblem definition : index
        result: List[str] = []
        def helper(index : int, slate: List) -> None:
            
            if index == len(s):
                result.append("".join(slate))
                return
            
            if s[index].isalpha():
                
                slate.append(s[index].upper())
                helper(index+1, slate)
                slate.pop()
                
                slate.append(s[index].lower())
                helper(index+1, slate)
                slate.pop()
            else:
                
                slate.append(s[index])
                helper(index+1, slate)
                slate.pop()
        
        helper(0,[])
        return result
    
        """
        TimeComplexity: In the worst case there can be all letters
        So each letter requires two cases lower and upper, it will take O(2^n)
        Copying the slate to the result array will take O(n).
        Overall : O(n*2^n)
        
        SpaceComplexity: There will be 2^n possibility and each will be of length n. 
        Overall : O(n*2^n)
        
        """
                
            
                