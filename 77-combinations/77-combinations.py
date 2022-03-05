class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result: List[int] = []
        def helper(first: int, slate:List[int]):
            
            if len(slate) == k:
                result.append(slate[:])
                return
    
            
            for i in range(first, n+1):
                
                slate.append(i)
                helper(i+1, slate)
                slate.pop()
            
            
            
        helper(1, [])
        return result