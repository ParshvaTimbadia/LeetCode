class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        
        minHeap = []
        for key, value in count.items():
            if len(minHeap) < k:
                heappush(minHeap, (value, key))
            elif minHeap[0][0] < value:
                heappop(minHeap)
                heappush(minHeap, (value, key))
        
        result = []
        while minHeap:
            result.append(heappop(minHeap)[1])
        
        return result
            
        
        
             