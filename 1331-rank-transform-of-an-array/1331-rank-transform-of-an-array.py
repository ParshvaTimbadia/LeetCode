class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        # O(NlogN) Solution and O(N) space.
        result = [0]*len(arr)
        minHeap = []
        
        
        for index, num in enumerate(arr):
            heappush(minHeap, (num, index))
        
        previous = None
        rank = 1
        while minHeap:
            num, index = heappop(minHeap)
            
            if previous == None or previous == num:
                result[index] = rank
            else:
                rank += 1
                result[index] = rank
            
            previous = num
        
        return result
            