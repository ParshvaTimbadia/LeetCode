class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        hMap = {}
        for index, num in enumerate(nums):
            
            if num in hMap:
                if abs(hMap[num] - index) <= k:
                    return True
            
            hMap[num] = index
        
        return False
    
        """
        TimeComplexity: O(N)
        SpaceComplexity: O(N)
        
        """
                