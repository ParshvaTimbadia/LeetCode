class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        end = max(piles)
        start = 1
        
        def calculateTotalHours(hours):
            result = 0
            for pile in piles:
                result += math.ceil(pile/hours)
            
            return result
        
        while start <= end:
            mid = start + (end - start)//2
            if calculateTotalHours(mid) <= h:
                end = mid - 1
            else:
                start = mid + 1
        
        return start