class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        start = 1
        end = max(piles)
        
        def calc(number_of_bananas):
            result = 0
            for b in piles:
                result += math.ceil(b/number_of_bananas)
            
            return result
        
        while start <= end:
            
            mid = start + (end-start)//2
            
            if calc(mid) <= h:
                #Mean koko can eat slow
                end = mid - 1
            else:
                start = mid + 1
        
        return start