class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        
        # One Box of candy to exchange. 
        # Total Candies Should be the same
        # result = [Alice must exchange, Bob must exchange]
        # The answer will exist.
        
        Sa, Sb = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        for x in aliceSizes:
            if (Sb - Sa)//2  + x in setB:
                return [x, (Sb - Sa)//2  + x]