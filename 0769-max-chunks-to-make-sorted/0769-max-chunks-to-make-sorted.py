class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        maxNumber = -1
        count = 0
        for index, number in enumerate(arr):
            maxNumber = max(maxNumber, number)
            if maxNumber == index:
                count += 1
            
        
        return count